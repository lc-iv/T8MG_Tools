import requests
from bs4 import BeautifulSoup
import pyttsx3

engine = pyttsx3.init()
search_item = 'jungle definition'  # search query

url = "https://www.google.com/search?q=" + search_item

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# I want to give a list or pd df of first 10 page results
# I want the text portion of the top result to be displayed

for item in soup.select(".st"):
    print(item.text)
    engine.say(item.text, 'en')
    engine.runAndWait()
    break


