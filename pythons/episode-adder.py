import ijson
import json
import time

# Start timing the operation
start_time = time.time()

# Path to your input JSON file (line-delimited JSON)
input_file = "C:/Users/User1/projects/AnimeRoman/pythons/files/export.json"

# Path to your output JSON file (valid JSON array)
output_file = "C:/Users/User1/projects/AnimeRoman/json/export.json"

# Function to process the JSON file and add episodes
def process_large_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        # Incrementally parse each JSON object from the input file
        parser = ijson.items(infile, 'item')  # 'item' to parse each object in the file
        
        # Open the output file as a JSON array
        outfile.write('[')
        
        first_entry = True  # Track if it's the first entry for formatting
        
        for item in parser:
            # Ensure the item is a dictionary
            if isinstance(item, dict):
                # Get episode count, and handle invalid values like 'fixme'
                episode_count = item.get("eposideCount", '0')  # Default to '0' if key is missing

                # If episode_count is a string like 'fixme', treat it as 0
                try:
                    episode_count = int(episode_count)
                except ValueError:
                    episode_count = 0  # Default to 0 if conversion fails

                # Add episode details
                item["episodes"] = [
                    {
                        "episodeNumber": i + 1,
                        "title": f"Episode {i + 1} Title",
                        "dubServer1": "#",
                        "dubServer2": "#",
                        "subServer1": "#",
                        "subServer2": "#"
                    }
                    for i in range(episode_count)
                ]
                
                # Write the entry to the output file, formatting as JSON with indentation
                if not first_entry:
                    outfile.write(',\n')  # Add a comma to separate entries
                first_entry = False  # After the first entry, use commas for subsequent entries
                
                # Dump the item (with the added episodes) to the output file
                json.dump(item, outfile, indent=4)
        
        # Close the JSON array
        outfile.write(']')

# Call the function
process_large_json(input_file, output_file)

# Print operation time
end_time = time.time()
print(f"Processing completed in {end_time - start_time:.2f} seconds.")
