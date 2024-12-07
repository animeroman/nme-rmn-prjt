import json

# Path to your input JSON file
input_file = "/content/drive/My Drive/Colab Notebooks/pythons/files/export_updated.json"

# Path to your output JSON file
output_file = "/content/drive/My Drive/Colab Notebooks/pythons/files/export_cmerged.json"

def normalize_type(type_str):
    """ Normalize the 'type' field to remove extra characters like parentheses. """
    if isinstance(type_str, str):
        # Remove parentheses around the type, if any, and strip extra spaces
        return type_str.strip().replace("(", "").replace(")", "")
    return type_str

def merge_connections(input_file, output_file):
    # Load JSON data
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    # Build a mapping of ID to entry for easy lookup
    id_to_entry = {item['id']: item for item in data}
    
    # Ensure each anime has itself as a connection
    for anime in data:
        if "connections" not in anime:
            anime["connections"] = []
        if not any(conn['id'] == anime['id'] for conn in anime['connections']):
            anime["connections"].append({"id": anime['id'], "type": anime['type']})

    # Function to propagate connections and return whether anything changed
    def propagate_connections():
        changes = False
        for anime in data:
            current_connections = anime['connections'][:]
            
            for connection in current_connections:
                connected_anime = id_to_entry.get(connection['id'])
                if connected_anime:
                    # Add anime's connections to the connected anime, if not already present
                    for conn in current_connections:
                        # Make sure connection is a dict and not a tuple or list
                        if isinstance(conn, dict):
                            if conn not in connected_anime['connections']:
                                connected_anime['connections'].append(conn)
                                changes = True
        return changes

    # Run the propagation process until no more changes
    while True:
        changes = propagate_connections()
        if not changes:
            break
    
    # Clean up connections by standardizing, removing duplicates, and normalizing the 'type'
    for anime in data:
        # Ensure that connections are all dictionaries and normalize the 'type'
        anime['connections'] = [
            {"id": conn['id'], "type": normalize_type(conn['type'])} if isinstance(conn, dict) else conn
            for conn in anime['connections']
        ]
        
        # Remove duplicates by converting the list to a set of tuples and back to a list
        unique_connections = {tuple(conn.items()) for conn in anime['connections']}
        anime['connections'] = [dict(conn) for conn in unique_connections]

    # Save the updated data back to a JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)

# Call the function to process the data
merge_connections(input_file, output_file)

print(f"Processing completed Seid. Updated data saved to {output_file}.")
