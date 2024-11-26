import ijson
import json
import time

# Start timing the operation
start_time = time.time()

# Path to your input JSON file
input_file = "C:/Users/User1/projects/AnimeRoman/pythons/files/export.json"

# Path to the output JSON file
output_file = "C:/Users/User1/projects/AnimeRoman/json/export.json"

# Function to process JSON file and add episodes
def process_large_json(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Parse the JSON file incrementally
        # Assuming the JSON starts with an array of items, so we use ijson.items to parse each object
        parser = ijson.items(infile, 'item')  # 'item' here is the element in the array
        
        for item in parser:
            # Ensure we are dealing with a dictionary and that 'eposideCount' exists
            if isinstance(item, dict):
                episode_count = item.get("eposideCount", 0)
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
                
                # Write processed JSON back to a file
                json.dump(item, outfile, indent=4)
                outfile.write('\n')  # Optional: Separate entries with a newline

# Call the function
process_large_json(input_file, output_file)

# Print operation time
end_time = time.time()
print(f"Processing completed in {end_time - start_time:.2f} seconds.")
