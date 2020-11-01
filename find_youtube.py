import requests
from bs4 import BeautifulSoup

import webbrowser

def findYT(search):
    words = search.split()

    search_link = "http://www.youtube.com/results?search_query=" + '+'.join(words)
    search_result = requests.get(search_link).text
    soup = BeautifulSoup(search_result, 'html.parser')
    videos = soup.select(".yt-uix-tile-link")
    if not videos:
        raise KeyError("No video found")
    link = "https://www.youtube.com" + videos[0]["href"]

    webbrowser.open_new(link)