import json
import os

# Load the JSON data from the file
file_path = 'C:/Users/aydin_000/Desktop/hiRoman/json/export.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Directory to save the HTML files
output_dir = 'C:/Users/aydin_000/Desktop/hiRoman/json/html_files/'
os.makedirs(output_dir, exist_ok=True)

# Loop through each entry in the JSON
for entry in data:
    # Get the page name
    page_name = entry.get('page', '')

    # Create the filename and path for the HTML file
    html_file_name = f"{page_name}.html"
    html_file_path = os.path.join(output_dir, html_file_name)

    # Write "789-630a" to each HTML file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write("789-630a")

    print(f"Created: {html_file_path}")

print("All HTML files have been created successfully.")
