import requests
from bs4 import BeautifulSoup
import ijson
import json
import time
import pickle
import os

# Base URL for fetching the anime page
base_url = "https://myanimelist.net/anime/"

# Path to save pickle progress
pickle_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/delete-after-finising/progress.pkl'

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
        genres_list, synonyms_list, japanese = [], [], None
        english, german, spanish, french = None, None, None, None
        studios_list, producers_list = [], []
        description = None
        connections_list = []

        # Scrape general details
        img_tag = soup.find('img', itemprop="image")
        poster_link = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None

        rating_tag = soup.find('span', itemprop="ratingValue")
        score = rating_tag.text.strip() if rating_tag else None

        # Scrape details from spaceit_pad divs
        spaceit_divs = soup.find_all('div', class_='spaceit_pad')
        for div in spaceit_divs:
            # Extract type, status, duration, season, rating, aired dates
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
                    duration_value = ' '.join(duration_text.split()[:2])  # First two parts
            
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
                    rating_value = rating_text.split(' - ')[0].strip()

            span_tag_aired = div.find('span', class_='dark_text', text="Aired:")
            if span_tag_aired:
                aired_text = span_tag_aired.next_sibling.strip() if span_tag_aired.next_sibling else None
                if aired_text:
                    dates = aired_text.split(' to ')
                    if len(dates) == 2:
                        date_start = dates[0].strip()
                        date_end = dates[1].strip()

            # Extract episode count
            span_tag_episodes = div.find('span', class_='dark_text', text="Episodes:")
            if span_tag_episodes:
                episodes_text = span_tag_episodes.next_sibling.strip() if span_tag_episodes.next_sibling else None
                if episodes_text and episodes_text.isdigit():
                    eposide_count = int(episodes_text)
            
            # Extract genres
            span_tag_genres = div.find('span', class_='dark_text', text="Genres:")
            if span_tag_genres:
                genre_links = div.find_all('a')
                genres_list = [genre.text.strip() for genre in genre_links if genre.text.strip()]

            # Extract synonyms
            span_tag_synonyms = div.find('span', class_='dark_text', text="Synonyms:")
            if span_tag_synonyms:
                synonyms_text = span_tag_synonyms.next_sibling.strip() if span_tag_synonyms.next_sibling else None
                if synonyms_text:
                    synonyms_list = [synonym.strip() for synonym in synonyms_text.split(',')]

            # Extract Japanese title
            span_tag_japanese = div.find('span', class_='dark_text', text="Japanese:")
            if span_tag_japanese:
                japanese = span_tag_japanese.next_sibling.strip() if span_tag_japanese.next_sibling else None

            # Extract studios
            span_tag_studios = div.find('span', class_='dark_text', text="Studios:")
            if span_tag_studios:
                studio_links = div.find_all('a')
                studios_list = [studio.text.strip() for studio in studio_links if studio.text.strip()]

            # Extract producers
            span_tag_producers = div.find('span', class_='dark_text', text="Producers:")
            if span_tag_producers:
                producer_links = div.find_all('a')
                producers_list = [producer.text.strip() for producer in producer_links if producer.text.strip()]

        # Extract alternative titles
        alt_titles_div = soup.find('div', class_='js-alternative-titles')
        if alt_titles_div:
            alt_spaceit_divs = alt_titles_div.find_all('div', class_='spaceit_pad')
            for div in alt_spaceit_divs:
                if div.find('span', class_='dark_text', text="English:"):
                    english = div.find('span', class_='dark_text', text="English:").next_sibling.strip()
                elif div.find('span', class_='dark_text', text="German:"):
                    german = div.find('span', class_='dark_text', text="German:").next_sibling.strip()
                elif div.find('span', class_='dark_text', text="Spanish:"):
                    spanish = div.find('span', class_='dark_text', text="Spanish:").next_sibling.strip()
                elif div.find('span', class_='dark_text', text="French:"):
                    french = div.find('span', class_='dark_text', text="French:").next_sibling.strip()

        # Handle connections from entries-table
        entries_table = soup.find('table', class_='entries-table')
        if entries_table:
            all_links = entries_table.find_all('a')
            for link in all_links:
                href = link.get('href', '')
                if '/anime/' in href:
                    try:
                        anime_id = href.split('/anime/')[1].split('/')[0]
                        li_parent = link.find_parent('li')
                        if li_parent:
                            type_text = li_parent.text.split('(')[-1].strip(')\n ')
                            connections_list.append({'id': anime_id, 'type': f"({type_text})"})
                    except IndexError:
                        continue

        # Handle connections from entries-tile
        entries_tile = soup.find('div', class_='entries-tile')
        if entries_tile:
            entry_divs = entries_tile.find_all('div', class_='entry')
            for entry_div in entry_divs:
                relation_div = entry_div.find('div', class_='relation')
                title_div = entry_div.find('div', class_='title')
                if relation_div and title_div:
                    try:
                        type_text = relation_div.text.split('(')[-1].strip(')\n ')
                        a_tag = title_div.find('a')
                        if a_tag and 'href' in a_tag.attrs:
                            href = a_tag['href']
                            anime_id = href.split('/anime/')[1].split('/')[0]
                            connections_list.append({'id': anime_id, 'type': f"({type_text})"})
                    except IndexError:
                        continue

        # Remove duplicates id from connections_list
        seen = set()
        unique_connections = []
        for connection in connections_list:
            conn_id = connection['id']
            if conn_id not in seen:
                unique_connections.append(connection)
                seen.add(conn_id)
        connections_list = unique_connections

        # Extract description
        description_tag = soup.find('p', itemprop="description")
        if description_tag:
            description = ''.join(description_tag.stripped_strings)

        title_tag = soup.find('h1', class_='title-name h1_bold_none')
        if title_tag:
            strong_tag = title_tag.find('strong')
            anime_original_value = strong_tag.text.strip() if strong_tag else None

        return (poster_link, score, type_value, status_value, duration_value, season_value, rating_value, anime_original_value, date_start, date_end, eposide_count, genres_list, synonyms_list, japanese, english, german, spanish, french, studios_list, producers_list, description, connections_list)
    except requests.HTTPError as http_err:
        print(f"HTTP error for ID {anime_id}: {http_err}")
    except Exception as e:
        print(f"Error fetching data for ID {anime_id}: {e}")
    return (None, None, None, None, None, None, None, None, None, None, None, [], [], None, None, None, None, None, [], [], None, [])

# Process the large JSON file
input_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/files/export_fixed.json'
output_file_path = '/content/drive/My Drive/Colab Notebooks/pythons/files/export_updated.json'

# Load progress if pickle file exists
if os.path.exists(pickle_file_path):
    with open(pickle_file_path, 'rb') as pickle_file:
        progress_data = pickle.load(pickle_file)
        updated_data = progress_data.get('updated_data', [])
        processed_ids = progress_data.get('processed_ids', set())
        print(f"Resuming from saved progress: {len(processed_ids)} entries processed.")
else:
    updated_data = []
    processed_ids = set()

# Read the input JSON file and process
with open(input_file_path, 'r', encoding='utf-8') as file:
    entries = list(ijson.items(file, 'item'))
    total_entries = len(entries)

    for idx, entry in enumerate(entries):
        anime_id = entry.get('id', '')
        if anime_id in processed_ids:
            continue  # Skip already processed entries
        
        if anime_id:
            # Fetch the details for the anime
            details = get_anime_details(anime_id)

            # Update the entry with fetched details
            if details:
                (poster_link, score, type_value, status_value, duration_value, season_value, rating_value, anime_original_value, date_start, date_end, eposide_count, genres_list, synonyms_list, japanese, english, german, spanish, french, studios_list, producers_list, description, connections_list) = details

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
                if eposide_count:
                    entry['eposideCount'] = eposide_count
                if genres_list:
                    entry['genres'] = genres_list
                if synonyms_list:
                    entry['synonyms'] = synonyms_list
                if japanese:
                    entry['japanese'] = japanese
                if english:
                    entry['english'] = english
                if german:
                    entry['german'] = german
                if spanish:
                    entry['spanish'] = spanish
                if french:
                    entry['french'] = french
                if studios_list:
                    entry['studios'] = studios_list
                if producers_list:
                    entry['producers'] = producers_list
                if description:
                    entry['description'] = description
                if connections_list:
                    entry['connections'] = connections_list

                # Append the updated entry to the list
                updated_data.append(entry)
                processed_ids.add(anime_id)

        # Save progress at halfway or every 100 items
        if idx % 100 == 0 or idx == total_entries // 2:
            with open(pickle_file_path, 'wb') as pickle_file:
                pickle.dump({'updated_data': updated_data, 'processed_ids': processed_ids}, pickle_file)
            print(f"Progress saved at {idx}/{total_entries} entries.")

        # Add a delay to avoid hitting the server too quickly
        time.sleep(1)  # Adjust the delay as needed

# Save the updated JSON data to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(updated_data, file, indent=4)

# Remove pickle file after successful completion
if os.path.exists(pickle_file_path):
    os.remove(pickle_file_path)

print("JSON file updated with poster links, scores, types, statuses, durations, seasons, ratings, animeOriginal, dateStart, dateEnd, eposideCount, genres, synonyms, japanese, english, german, spanish, french, studios, producers, description, and connections.")
