import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

page = requests.get("https://www.youridioms.com/en/idiom/lick-ones-chops")
soup = BeautifulSoup(page.content, 'html.parser')
# wrapper = soup.find(id='gatsby-focus-wrapper')
wrapper = soup.find('body')
# print(wrapper)

# images = wrapper.find_all("img", class_='align-self-start max-h-20')
images = wrapper.find_all("img")
for image in images:
    imgData = image.get('data-src')
    filename = ''
    imgUrl = ''

    if imgData: 
        imgData
    else:
        imgData = image['src']
    
    filename = imgData.split('/')[-1]
    imgUrl = "https://www.youridioms.com" + imgData

    print(imgUrl)
    urllib.request.urlretrieve(imgUrl, "./downloaded_img/"+ filename)



