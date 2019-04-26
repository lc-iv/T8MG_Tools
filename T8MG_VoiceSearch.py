# T8MG Voice Search: I use it to search talent
# Louis     = dict[Python Programmer, Music Publisher, Freelancer]
# Github    = lc-iv
# email     = louismcoinley@gmail.com
# wechat    = k_louis_iv

import requests
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
from fake_useragent import UserAgent
import pandas as pd

# Create engine for voice playback
engine = pyttsx3.init()
ua = UserAgent()
r           = sr.Recognizer()
mic         = sr.Microphone()
t3x         = r.recognize_google

# Create search item variable
with mic as source:
    print('What\'s up?!')
    audio  = r.listen(source)
    print('Done!')

text        = t3x(audio)
search_item = text  # search query
num_result  = 10

# Create url variable directing to search engine + search_item
url = "https://www.google.com/search?q=" + search_item + '&num=' + str(num_result)

# Pull requests
response    = requests.get(url, {"User-Agent": ua.random})
soup        = BeautifulSoup(response.text, "html.parser")
result_div  = soup.find_all('div', attrs={'class': 'g'})


# Combine and package results in lists
links       = []
titles      = []
description = []
for r in result_div:
    # Checks if each element is present, else, raise exception
    try:
        link        = r.find('a', href=True)
        title       = r.find('h3', attrs={'class': 'r'}).get_text()
        description = r.find('span', attrs={'class': 'st'}).get_text()

        # Check to make sure everything is present before appending
        if link != '' and title != '' and description != '':
            links.append(link['href'])
            titles.append(title)
            descriptions.append(description)
    # Next loop if one element is not present
    except:
        continue

# Organize search results into pd df
Search_Results = pd.DataFrame({'Links': links,
                               'Titles': titles,
                               'Descriptions': description
                               })

# Right now most links are giving 404 errors
print(Search_Results.head())

# Voice playback
for item in soup.select(".g"):
    print(item.text)
    engine.say(item.text, 'en')
    engine.runAndWait()
    break



