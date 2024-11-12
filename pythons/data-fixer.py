import ijson
import json
import time

# Manually set the file paths for input and output files
input_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/files/export.json'
output_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/files/export_fixed.json'

# Initialize the converted data list
converted_data = []

# Open the input JSON file and use ijson to parse it incrementally
with open(input_file_path, 'r') as infile:
    # Parse the 'Watching' array in the input JSON file
    watching_items = ijson.items(infile, 'Watching.item')

    for anime in watching_items:
        # Extract the ID from the 'link' and remove the prefix
        anime_id = anime["link"].replace("https://myanimelist.net/anime/", "")
        
        # Print the ID being processed
        print(f"Fetching data for id: {anime_id}")
        
        # Create the converted entry
        converted_entry = {
            "id": anime_id,
            "animeEnglish": anime["name"],
            "animeOriginal": "Original Name",
            "duration": "min.",
            "type": "type",
            "status": "status",
            "rated": "R",
            "score": "10",
            "season": "season",
            "language": "SUB & DUB",
            "dateStart": "date",
            "dateEnd": "date",
            "poster": "link.jpg",
            "page": "pagelink",
            "subCount": "3",
            "dubCount": "3",
            "episodes": [
                {
                    "episodeNumber": 1,
                    "title": "Episode 1 Title",
                    "dubServer1": "#",
                    "dubServer2": "#",
                    "subServer1": "#",
                    "subServer2": "#"
                },
                {
                    "episodeNumber": 2,
                    "title": "Episode 2 Title",
                    "dubServer1": "#",
                    "dubServer2": "#",
                    "subServer1": "#",
                    "subServer2": "#"
                },
                {
                    "episodeNumber": 3,
                    "title": "Episode 3 Title",
                    "dubServer1": "#",
                    "dubServer2": "#",
                    "subServer1": "#",
                    "subServer2": "#"
                }
            ]
        }
        
        # Append the converted entry to the list
        converted_data.append(converted_entry)

# Save the converted data to 'anvenced-data.json' in one go
with open(output_file_path, 'w') as outfile:
    json.dump(converted_data, outfile, indent=4)

print("Conversion complete! Data saved to 'anvenced-data.json'.")
