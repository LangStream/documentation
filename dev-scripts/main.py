import json
import argparse
import os
import html


def escape_html(text, link = None):
    if type(text) == bool:
        if text:
            return "✓"
        else:
            return ""
    if not text:
        return ''
    text = str(text)
    text = html.escape(text).replace('\n', '<br>')
    if link:
        return f"<a href=\"{link}\">{text}</a>"
    return text
    


def generate_single_entity_table(entity_name, entity_ref, description, properties, is_nested=False):
    result = []
    if is_nested:
        table = f"<br><h3 data-full-width=\"true\"><a name=\"{entity_ref}\"></a>{entity_name}</h3>"
    else:
        table = f"<br><h2 data-full-width=\"true\"><a name=\"{entity_ref}\"></a>{entity_name}</h2>"

    if description:
        table += f"<p data-full-width=\"true\">{escape_html(description)}</p>\n\n"

    table += "<table data-full-width=\"true\">"
    table += "<thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody>"

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
            table += f"<tr><td><code>{escape_html(key)}</code></td><td>{escape_html(value.get('description', ''))}</td><td>{escape_html(prop_type, link)}</td><td>{escape_html(value.get('required', ''))}</td><td>{escape_html(value.get('defaultValue', ''))}</td></tr>"
    
    table += "</tbody></table>\n\n"

    result.append(table)

    if properties:
        for key, value in properties.items():
            nested_properties = value.get('properties', {})
            if nested_properties:
                nested_tables = generate_single_entity_table(f"{entity_name}.{key}", f"{entity_ref}.{key}", '', nested_properties, True)
                result.extend(nested_tables)
            items = value.get('items', {})
            if items and items.get('properties', {}):
                result.extend(generate_single_entity_table(f"{entity_name}.{key}", f"{entity_ref}.{key}", '', items.get('properties', {}), True))

    return result

def generate_entity_tables(title, version, data, output_file):

    content = f"<h1>{title}</h1>"
    content += f"<p>LangStream Version: <strong>{version}</strong></p>\n\n"
    content += gen_entity(data)
            
    with open(output_file, 'w') as file:
        file.write(content)

    print(f"Tables generated and saved to {output_file}")

def gen_entity(data):
    content = "\n\n"

    for key, value in data.items():
        if value:
            label = f"{value.get('name')} (<code>{value.get('type', key)}</code>)"
            tables = generate_single_entity_table(label, key, value.get('description', ''), value.get("properties", {}))
            for nested_table in tables:
                content += nested_table
    content += "\n\n"
    return content

def main():
    parser = argparse.ArgumentParser(description='Generate HTML tables from JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_directory', type=str, help='Path to save the output HTML file')

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
