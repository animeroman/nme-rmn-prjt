import ijson
import json
import re
import time

# Start timing the operation
start_time = time.time()

# Path to your input JSON file
input_file_path = 'C:/Users/User1/projects/RomanAPI/export.json'

# Path to your output JSON file
output_file_path = 'C:/Users/User1/projects/AnimeRoman/json/export.json'

# Function to process animeEnglish and generate the 'page' link, including the 'id'
def generate_page_link(anime_english, anime_id):
    # Convert to lowercase
    anime_english = anime_english.lower()
    # Replace spaces with hyphens
    anime_english = anime_english.replace(' ', '-')
    # Remove special characters (including Unicode symbols)
    anime_english = re.sub(r'[^a-z0-9-]', '', anime_english)
    # Append the ID to the page link
    return f"{anime_english}-{anime_id}"

# Process the JSON file incrementally
def process_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        # Incrementally parse each JSON object
        parser = ijson.items(infile, 'item')  # Parse each JSON object from the file

        # Open the output file as a JSON array
        outfile.write('[')
        first_entry = True

        for entry in parser:
            # Skip malformed or non-dict entries
            if not isinstance(entry, dict):
                continue

            # Process the 'animeEnglish' field and generate the 'page' link
            anime_english = entry.get('animeEnglish', '')
            anime_id = entry.get('id', '')
            entry['page'] = generate_page_link(anime_english, anime_id)

            # Write the entry to the output file
            if not first_entry:
                outfile.write(',\n')
            json.dump(entry, outfile, indent=4)
            first_entry = False

        # Close the JSON array
        outfile.write(']')

# Call the processing function
process_json(input_file_path, output_file_path)

# Print operation time
end_time = time.time()
print(f"Processing complete. The modified JSON has been saved. Time taken: {end_time - start_time:.2f} seconds.")
