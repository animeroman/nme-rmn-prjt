import json
import re

# Make sure to use the correct path to your JSON file
file_path = 'C:/Users/aydin_000/Desktop/hiRoman/json/export_updater.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to process animeEnglish
def generate_page_link(anime_english):
    # Convert to lowercase
    anime_english = anime_english.lower()
    # Replace spaces with hyphens
    anime_english = anime_english.replace(' ', '-')
    # Remove special characters
    anime_english = re.sub(r'[\'.,/;:<>?\[\]{}\\|!@$#%^&*()]', '', anime_english)
    return anime_english

# Update the 'page' field with the processed 'animeEnglish'
for entry in data:
    anime_english = entry.get('animeEnglish', '')
    page_link = generate_page_link(anime_english)
    entry['page'] = page_link

# Save the modified JSON back to a file
output_file_path = 'C:/Users/aydin_000/Desktop/hiRoman/json/export_modified.json'

with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print("Processing complete. The modified JSON has been saved.")
