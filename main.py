
from datetime import date
import os
from ytmusicapi import YTMusic
import requests
from bs4 import BeautifulSoup

# Check for browser.json
if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print(" Linux: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

#Scraping the top 100 songs playlist
input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://appbrewery.github.io/bakeboard-hot-100/{input_date}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")


song_names = soup.find_all(name="h3", class_="chart-entry__title")
song_names = [song.getText().strip() for song in song_names]
songs = song_names[::-1]

#YouTube Music Authentication
yt = YTMusic("browser.json")

#Create playlist name based on input date
PLAYLIST_NAME = f"{input_date} Billboard 100"
playlist_id = yt.create_playlist(
    PLAYLIST_NAME,
    f"Top songs from {input_date}",
    privacy_status="PRIVATE",
)
print(f"Created playlist: {PLAYLIST_NAME}")

for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")