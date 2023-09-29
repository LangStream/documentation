import json
import argparse


def escape_markdown(text):
    if type(text) == bool:
        if text:
            return "✓"
        else:
            return ""
    if not text:
        return ''
    text = str(text)
    return text.replace('|', '\|').replace('\n', '<br>')


def generate_agent_table(agent_name, properties, is_nested=False):
    result = []
    if is_nested:
        table = f"\n\n#### <a name=\"{agent_name}\"></a>{agent_name}\n\n"
    else:
        table = f"\n\n### {agent_name}\n\n"
    table += "| Key | Description | Type | Required | Default Value |\n"
    table += "| --- | --- | --- | --- | --- |\n"

    if properties:
        for key, value in properties.items():
            prop_type = value.get('type', '')
            if prop_type == "array":
                items = value.get('items', {})
                if items:
                    if items.get('type', '') == "object":
                        link = f"{agent_name}.{key}"
                        prop_type = f"array of [object](#{link})"
                    else:
                        prop_type = f"array of {items.get('type', '')}"
            table += f"| {escape_markdown(key)} | {escape_markdown(value.get('description', ''))} | {escape_markdown(prop_type)} | {escape_markdown(value.get('required', ''))} | {escape_markdown(value.get('defaultValue', ''))} |\n"

    result.append(table)

    if properties:
        for key, value in properties.items():
            nested_properties = value.get('properties', {})
            if nested_properties:
                nested_tables = generate_agent_table(f"{agent_name}.{key}", nested_properties, is_nested)
                result.extend(nested_tables)
            items = value.get('items', {})
            if items and items.get('properties', {}):
                result.extend(generate_agent_table(f"{agent_name}.{key}", items.get('properties', {}), True))

    return result

def generate_agent_tables(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    agents_data = data.get('agents', {})

    markdown_content = "# API Reference\n\n"
    markdown_content += "## Agents\n\n"
    markdown_content += "| ID | Name | Description |\n"
    markdown_content += "| --- | --- | --- |\n"

    for agent_name, agent_data in agents_data.items():
        markdown_content += f"| [{escape_markdown(agent_name)}](#{agent_name}) | {escape_markdown(agent_data.get('name', ''))} | {escape_markdown(agent_data.get('description', ''))} |\n"

    for agent_name, agent_data in agents_data.items():
        if agent_data:
            tables = generate_agent_table(agent_name, agent_data.get("properties", {}))
            for nested_table in tables:
                markdown_content += nested_table


            

    # Save the Markdown content to a file
    with open(output_file, 'w') as file:
        file.write(markdown_content)

    print(f"Markdown tables generated and saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_file', type=str, help='Path to save the output Markdown file')

    args = parser.parse_args()

    generate_agent_tables(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
