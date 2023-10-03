import json
import argparse
import os


def escape_markdown(text, link = None):
    if type(text) == bool:
        if text:
            return "✓"
        else:
            return ""
    if not text:
        return ''
    text = str(text)
    text = text.replace('|', '\|').replace('\n', '<br>')
    if link:
        return f"<a href=\"{link}\">{text}</a>"
    return text
    


def generate_single_entity_table(entity_name, entity_ref, description, properties, is_nested=False):
    result = []
    if is_nested:
        table = f"\n\n#### <a name=\"{entity_ref}\"></a>{entity_name}\n\n"
    else:
        table = f"\n\n### <a name=\"{entity_ref}\"></a>{entity_name}\n\n"

    if description:
        table += f"{escape_markdown(description)}\n\n"

    table += "|  | Description | Type | Required | Default Value |\n"
    table += "| --- | --- | --- | --- | --- |\n"

    if properties:
        for key, value in properties.items():
            prop_type = value.get('type', '')
            link = ""
            if prop_type == "array":
                items = value.get('items', {})
                if items:
                    if items.get('type', '') == "object":
                        link = f"#{entity_ref}.{key}"
                        prop_type = f"array of object"
                    else:
                        prop_type = f"array of {items.get('type', '')}"
            table += f"| `{escape_markdown(key)}` | {escape_markdown(value.get('description', ''))} | {escape_markdown(prop_type, link)} | {escape_markdown(value.get('required', ''))} | {escape_markdown(value.get('defaultValue', ''))} |\n"

    result.append(table)

    if properties:
        for key, value in properties.items():
            nested_properties = value.get('properties', {})
            if nested_properties:
                nested_tables = generate_single_entity_table(f"{entity_name}.{key}", f"{entity_ref}.{key}", '', nested_properties, is_nested)
                result.extend(nested_tables)
            items = value.get('items', {})
            if items and items.get('properties', {}):
                result.extend(generate_single_entity_table(f"{entity_name}.{key}", f"{entity_ref}.{key}", '', items.get('properties', {}), True))

    return result

def generate_entity_tables(title, version, data, output_file):

    markdown_content = f"# {title}\n\n"
    markdown_content += f"LangStream Version: **{version}**\n\n"
    markdown_content += gen_entity(title, data)
            
    with open(output_file, 'w') as file:
        file.write(markdown_content)

    print(f"Markdown tables generated and saved to {output_file}")

def gen_entity(title, data):
    if title:
        markdown_content = f"## {title}\n\n"
    else: 
        markdown_content = ""
    markdown_content += "| Name | Type |\n"
    markdown_content += "| --- | --- |\n"

    for key, value in data.items():
        label = value.get('type', key)
           
        link = f"#{key}"
        name = value.get('name', '')
        markdown_content += f"| {escape_markdown(name, link)} | {escape_markdown(label)} |\n"

    for key, value in data.items():
        if value:
            label = f"{value.get('name')} (`{value.get('type', key)}`)"
            tables = generate_single_entity_table(label, key, value.get('description', ''), value.get("properties", {}))
            for nested_table in tables:
                markdown_content += nested_table
    markdown_content += "\n\n"
    return markdown_content

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_directory', type=str, help='Path to save the output Markdown file')

    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        data = json.load(file)

    agents_data = data.get('agents', {})
    resources_data = data.get('resources', {})
    assets_data = data.get('assets', {})
    version = data.get('version', '?')

    generate_entity_tables("Agents", version, agents_data, os.path.join(args.output_directory, 'agents.md'))
    generate_entity_tables("Resources", version, resources_data, os.path.join(args.output_directory, 'resources.md'))
    generate_entity_tables("Assets", version, assets_data, os.path.join(args.output_directory, 'assets.md'))

if __name__ == '__main__':
    main()
