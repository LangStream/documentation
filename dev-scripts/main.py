import json
import argparse

def generate_agent_table(agent_name, agent_data):
    table = f"<h3 id={agent_name}>{agent_name}</h3>"
    table += "<table>"

    properties = agent_data.get('properties', {})
    if properties:
        table += generate_properties_table(properties)

    table += "</table>"
    nested_tables = []

    return table, nested_tables

def generate_properties_table(properties):
    table = "<table>"

    # Properties table headers
    table += "<tr><th>Key</th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr>"

    for key, value in properties.items():
        table += "<tr>"
        table += f"<td>{key}</td>"
        table += f"<td>{value.get('description', '')}</td>"
        table += f"<td>{value.get('type', '')}</td>"
        table += f"<td>{value.get('required', '')}</td>"
        table += f"<td>{value.get('defaultValue', '')}</td>"
        table += "</tr>"

        nested_properties = value.get('properties', {})
        if nested_properties:
            nested_table = generate_properties_table(nested_properties)
            table += f"<tr><td colspan='5'>{nested_table}</td></tr>"

    table += "</table>"
    return table

def generate_agent_tables(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    agents_data = data.get('agents', {})

    # Generate HTML tables for each agent entry
    html_content = "<h2>Agents</h2><table>"
    html_content += "<tr><th>ID</th><th>Name</th><th>Description</th></tr>"

    
    for agent_name, agent_data in agents_data.items():

        html_content += "<tr>"
        html_content += f"<td><a href=\"{agent_name}\">{agent_name}</a></td>"
        html_content += f"<td>{agent_data.get('name', '')}</td>"
        html_content += f"<td>{agent_data.get('description', '')}</td>"
        html_content += "</tr>"
        

    html_content += "</table>"

    for agent_name, agent_data in agents_data.items():
        if agent_data:
            table, nested_tables = generate_agent_table(agent_name, agent_data)
            html_content += table

            # Append nested tables after the current agent's table
            for nested_table in nested_tables:
                html_content += nested_table

    # Save the HTML content to a file
    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f"HTML tables generated and saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate HTML tables from JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_file', type=str, help='Path to save the output HTML file')

    args = parser.parse_args()

    generate_agent_tables(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
