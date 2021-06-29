import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

page = requests.get("https://www.thtventures.org/portfolio")
soup = BeautifulSoup(page.content, 'html.parser')
wrapper = soup.find(id='gatsby-focus-wrapper')
# print(week)

images = wrapper.find_all("img", class_='align-self-start max-h-20')
for image in images:
    filename = image['src'].split('/')[-1]
    urllib.request.urlretrieve(image['src'], "./downloaded_img/"+ filename)



