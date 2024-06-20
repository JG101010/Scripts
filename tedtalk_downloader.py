import requests #getting content of the TED talk page

from bs4 import BeautifulSoup #web scraping

import re #Regular Expression pattern matching

# from urllib.request import urlretrieve #downloading mp4

import sys #for argument parsing

# Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

#url = "https://www.ted.com/talks/cordae_how_a_hi_level_mindset_helps_you_realize_your_potential"
#url = "https://www.ted.com/talks/michael_tilson_thomas_music_and_emotion_through_time"
    
r = requests.get(url)

print ("Download about to start")

soup = BeautifulSoup(r.content, features="xml)")

for val in soup.find_All("script"):
    )