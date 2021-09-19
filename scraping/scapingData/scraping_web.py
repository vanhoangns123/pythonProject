import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://nha.chotot.com/ha-noi/quan-hai-ba-trung/phuong-vinh-tuy/mua-ban-bat-dong-san?price=1000000000-*")
soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all(class_='wrapperAdItem___2woJ1')

results = []
for item in items:
    # title
    title = item.find(class_='adTitle___3SoJh').get_text()
    # space in m2
    space = item.find(class_='adItemCondition___2daw2').get_text().split()[0]
    # price in billion
    price = item.find(class_='adPriceNormal___puYxd').get_text().split()[0]
    # price by square
    if "," in price:
        price = float(price.replace(',', '.')) * 1000000000
    result = round(float(price) / float(space))
    if result > 0 :
        print(result)
        results.append(result)

print(results)
print(max(results))
print(min(results))