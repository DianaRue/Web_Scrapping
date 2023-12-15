from bs4 import BeautifulSoup
import requests
import html5lib
import re

url = "https://www.mohcc.gov.zw/"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

all_urls = [a['href']
            for a in soup('a')
            if a.has_attr('href')]

print(len(all_urls))

# l want the url with the mental health info 
regex = r"https?://.*\.mentalheaalth\.gov/?$"
            