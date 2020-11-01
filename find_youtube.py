import requests
from bs4 import BeautifulSoup
import re

import webbrowser

def findYT(search):
    words = search.split()

    search_link = "http://www.youtube.com/results?search_query=" + '+'.join(words)
    search_result = requests.get(search_link).text
    soup = BeautifulSoup(search_result, 'html.parser').text
    video_pattern = re.compile(r"watch\?v=(\S{11})")
    video_ids = re.findall(video_pattern,soup)
    webbrowser.open("https://www.youtube.com/watch?v="+video_ids[0])

