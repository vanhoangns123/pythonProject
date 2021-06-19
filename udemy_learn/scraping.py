import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.436890000000062&lon=-66.11155999999994")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
# print(week)

items = week.find_all(class_='tombstone-container')
period_name = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

print(period_name)
print(short_desc)
print(type(short_desc))
print(temp)


weather_stuff = pd.DataFrame({
    'period': period_name,
    'short_desc': short_desc,
    'temp': temp,
 })

print(weather_stuff)
