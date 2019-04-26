# T8MG Voice Search
# Louis     = dict[Python Programmer, Music Publisher, Freelancer]
# Github    = lc-iv
# email     = louismcoinley@gmail.com
# wechat    = k_louis_iv

import requests
from bs4 import BeautifulSoup
import pyttsx3

# Create engine for voice playback
engine = pyttsx3.init()

# Create search item variable
search_item = 'jungle definition'  # search query

# Create url variable directing to search engine + search_item
url = "https://www.google.com/search?q=" + search_item

# Pull requests
response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")
soup = BeautifulSoup(response.content, "html.parser")

# I want to give a list or pd df of first 10 page results
# I want the text portion of the top result to be displayed
# url = soup.h3.a['href'][7:].split('&')
# print(url[0])

for item in soup.select(".st"):
    print(item.text)
    # engine.say(item.text, 'en')
    # engine.runAndWait()
    break


