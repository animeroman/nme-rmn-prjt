import requests
from bs4 import BeautifulSoup
import ijson
import json
import time

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
        rating_value, anime_original_value, date_start, date_end = None, None, None, None

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

        title_tag = soup.find('h1', class_='title-name h1_bold_none')
        if title_tag:
            strong_tag = title_tag.find('strong')
            anime_original_value = strong_tag.text.strip() if strong_tag else None

        return (poster_link, score, type_value, status_value, duration_value, season_value, rating_value, anime_original_value, date_start, date_end)
    except requests.HTTPError as http_err:
        print(f"HTTP error for ID {anime_id}: {http_err}")
    except Exception as e:
        print(f"Error fetching data for ID {anime_id}: {e}")
    return (None, None, None, None, None, None, None, None, None, None)

# Process the large JSON file
input_file_path = 'C:/Users/aydin_000/Desktop/hiRoman/json/export.json'
output_file_path = 'C:/Users/aydin_000/Desktop/hiRoman/json/export_updated.json'

updated_data = []

with open(input_file_path, 'r', encoding='utf-8') as file:
    # Use ijson to load JSON objects incrementally
    for entry in ijson.items(file, 'item'):
        anime_id = entry.get('id', '')
        if anime_id:
            # Fetch the details for the anime
            details = get_anime_details(anime_id)

            # Update the entry with fetched details
            if details:
                (poster_link, score, type_value, status_value, duration_value, season_value, rating_value, anime_original_value, date_start, date_end) = details

                if poster_link:
                    entry['poster'] = poster_link
                if score:
                    entry['score'] = score
                if type_value:
                    entry['type'] = type_value
                if status_value:
                    entry['status'] = status_value
                if duration_value:
                    entry['duration'] = duration_value
                if season_value:
                    entry['season'] = season_value
                if rating_value:
                    entry['rated'] = rating_value
                if anime_original_value:
                    entry['animeOriginal'] = anime_original_value
                if date_start:
                    entry['dateStart'] = date_start
                if date_end:
                    entry['dateEnd'] = date_end

                # Append the updated entry to the list
                updated_data.append(entry)
            
            # Add a delay to avoid hitting the server too quickly
            time.sleep(1)  # Adjust the delay as needed

# Save the updated JSON data to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(updated_data, file, indent=4)

print("JSON file updated with poster links, scores, types, statuses, durations, seasons, ratings, animeOriginal, dateStart, and dateEnd.")
