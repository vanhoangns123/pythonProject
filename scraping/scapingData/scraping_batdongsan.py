import requests
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import cloudscraper
import fake_proxy

area='-hgi'
wards=[
    '-chau-thanh',
    '-chau-thanh-a',
    '-long-my',
    '-phung-hiep',
    '-vi-thuy',
    '-nga-bay',
    '-vi-thanh',
    '-thi-xa-long-my'
]

# https://batdongsan.com.vn/ban-dat-chau-thanh-hgi
# https://batdongsan.com.vn/ban-dat-nen-du-an-chau-thanh-hgi

# https://batdongsan.com.vn/ban-nha-rieng-chau-thanh-hgi
# https://batdongsan.com.vn/ban-nha-mat-pho-chau-thanh-hgi

types=[
    'ban-dat',
    'bat-dat-nen-du-an',
    'ban-nha-rieng',
    'ban-nha-mat-pho'
]

ua = UserAgent()
scraper = cloudscraper.create_scraper()
data_table = []
proxies = fake_proxy.get(amount=3, proxy_type='https')
print(proxies)
proxies = {
    'https': proxies[0]['ip']+':'+proxies[0]['port']
}
print(proxies)

for ward in wards:
    for type in types:
        url = "https://batdongsan.com.vn/"+type+ward+area
        headers = {
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'User-Agent': ua.random,
            # 'referer': url
        }
        # page = requests.get(url, headers=headers, proxies=proxies).content
        page = scraper.get(url, proxies=proxies).text
        print(page)
        # print(page.content)
        # print(page.content.decode())

        soup = BeautifulSoup(page, 'html.parser')
        week = soup.find(id='product-lists-web')

        items = soup.find_all(class_='product-item')
        for item in items:
            price = item.find(class_='price').get_text()
            dt = item.find(class_='area').get_text()
            dis = item.find(class_='location').get_text()
            data_table.append({'price': price,
                                'dt': dt,
                                'dis': dis,
                                'type': type,
                                'ward': ward})

dataframe = pd.DataFrame(data=data_table)
print(dataframe)
dataframe.to_excel("batdongsan_haugiang.xlsx", engine='xlsxwriter')