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
            "animeOriginal": "fixme",
            "duration": "fixme",
            "type": "fixme",
            "status": "fixme",
            "rated": "fixme",
            "score": "fixme",
            "season": "fixme",
            "language": "fixme",
            "dateStart": "fixme",
            "dateEnd": "fixme",
            "poster": "fixme",
            "page": "fixme",
            "subCount": "fixme",
            "dubCount": "fixme"
        }
        
        # Append the converted entry to the list
        converted_data.append(converted_entry)

# Save the converted data to 'anvenced-data.json' in one go
with open(output_file_path, 'w') as outfile:
    json.dump(converted_data, outfile, indent=4)

print("Conversion complete! Data saved to 'anvenced-data.json'.")
