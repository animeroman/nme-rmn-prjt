import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import pickle
import os

# Base URL for fetching the anime page
base_url = "https://myanimelist.net/anime/"

# Function to scrape anime details
def get_anime_details(anime_id):
    try:
        # Construct the URL
        url = f"{base_url}{anime_id}"
        print(f"Fetching data for URL: {url}")  # Print the URL for debugging

        # Set a user-agent header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send a GET request to fetch the page content
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize variables for various fields
        poster_link, score, type_value = None, None, None
        status_value, duration_value, season_value = None, None, None
        rating_value, anime_original_value, date_start, date_end, eposide_count = None, None, None, None, None
        genres_list = []

        # Find details
        img_tag = soup.find('img', itemprop="image")
        poster_link = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None

        rating_tag = soup.find('span', itemprop="ratingValue")
        score = rating_tag.text.strip() if rating_tag else None

        spaceit_divs = soup.find_all('div', class_='spaceit_pad')
        for div in spaceit_divs:
            # Check various details (type, status, duration, etc.)
            span_tag_type = div.find('span', class_='dark_text', text="Type:")
            if span_tag_type:
                a_tag = div.find('a')
                type_value = a_tag.text.strip() if a_tag else None
            
            span_tag_status = div.find('span', class_='dark_text', text="Status:")
            if span_tag_status:
                status_value = span_tag_status.next_sibling.strip() if span_tag_status.next_sibling else None
            
            span_tag_duration = div.find('span', class_='dark_text', text="Duration:")
            if span_tag_duration:
                duration_text = span_tag_duration.next_sibling.strip() if span_tag_duration.next_sibling else None
                if duration_text:
                    duration_value = ' '.join(duration_text.split()[:2])  # Get the first two parts
            
            span_tag_season = div.find('span', class_='dark_text', text="Premiered:")
            if span_tag_season:
                a_tag = div.find('a')
                if a_tag:
                    season_text = a_tag.text.strip()
                    season_value = season_text.split()[0] if season_text else None
            
            span_tag_rating = div.find('span', class_='dark_text', text="Rating:")
            if span_tag_rating:
                rating_text = span_tag_rating.next_sibling.strip() if span_tag_rating.next_sibling else None
                if rating_text:
                    rating_value = rating_text.split(' - ')[0].strip()  # Get the first part

            span_tag_aired = div.find('span', class_='dark_text', text="Aired:")
            if span_tag_aired:
                aired_text = span_tag_aired.next_sibling.strip() if span_tag_aired.next_sibling else None
                if aired_text:
                    dates = aired_text.split(' to ')
                    if len(dates) == 2:
                        date_start = dates[0].strip()  # First date
                        date_end = dates[1].strip()  # Second date

            # Handle eposideCount
            span_tag_episodes = div.find('span', class_='dark_text', text="Episodes:")
            if span_tag_episodes:
                episodes_text = span_tag_episodes.next_sibling.strip() if span_tag_episodes.next_sibling else None
                if episodes_text and episodes_text.isdigit():
                    eposide_count = int(episodes_text)
            
            # Handle genres
            span_tag_genres = div.find('span', class_='dark_text', text="Genres:")
            if span_tag_genres:
                genre_links = div.find_all('a')
                genres_list = [genre.text.strip() for genre in genre_links if genre.text.strip()]

        title_tag = soup.find('h1', class_='title-name h1_bold_none')
        if title_tag:
            strong_tag = title_tag.find('strong')
            anime_original_value = strong_tag.text.strip() if strong_tag else None

        return {
            "poster": poster_link,
            "score": score,
            "type": type_value,
            "status": status_value,
            "duration": duration_value,
            "season": season_value,
            "rated": rating_value,
            "animeOriginal": anime_original_value,
            "dateStart": date_start,
            "dateEnd": date_end,
            "eposideCount": eposide_count,
            "genres": genres_list
        }
    except requests.HTTPError as http_err:
        print(f"HTTP error for ID {anime_id}: {http_err}")
    except Exception as e:
        print(f"Error fetching data for ID {anime_id}: {e}")
    return {}

# Process the large JSON file using pandas
input_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/files/export_fixed.json'
output_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/files/export_updated.json'
pickle_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/delete-after-finising/progress.pkl'

# Load the JSON data into a pandas DataFrame
data = pd.read_json(input_file_path)

# Check if there is saved progress (from previous runs)
if os.path.exists(pickle_file_path):
    with open(pickle_file_path, 'rb') as f:
        processed_ids = pickle.load(f)
else:
    processed_ids = set()

# Update each entry with the new details
updated_entries = []
for _, row in data.iterrows():
    anime_id = row.get("id", "")
    
    if anime_id and anime_id not in processed_ids:
        details = get_anime_details(anime_id)
        if details:
            for key, value in details.items():
                if value is not None:
                    row[key] = value
            processed_ids.add(anime_id)
        
        # Save progress every 20 entries
        if len(processed_ids) % 20 == 0:
            with open(pickle_file_path, 'wb') as f:
                pickle.dump(processed_ids, f)

    updated_entries.append(row)

# Convert the updated entries back to a DataFrame
updated_data = pd.DataFrame(updated_entries)

# Save the updated DataFrame to a new JSON file
updated_data.to_json(output_file_path, orient='records', indent=4)

print("JSON file updated with all fields using pandas. Progress saved with pickle.")
