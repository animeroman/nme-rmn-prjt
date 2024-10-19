import os
from bs4 import BeautifulSoup

# Directory containing the HTML files
folder_path = 'C:/Users/aydin_000/projects/nme-rmn-prjt/genre'  # Update this path

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)
        
        # Open and read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        
        # Find all div elements with class that includes "some-lorem"
        for div in soup.find_all('div', class_=lambda c: c and 'film_list-wrap' in c.split()):
            # Clear the content of the div without removing the div itself
            div.clear()  # This clears all content inside the div but keeps the div tag intact

        # Save the modified HTML back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            # Use the prettify() method to maintain proper formatting (optional)
            file.write(str(soup))

print("HTML content inside 'some-lorem' divs cleared successfully without damaging the code structure.")
