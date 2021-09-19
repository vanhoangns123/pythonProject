import requests
import pandas as pd
from bs4 import BeautifulSoup

# '/hau-giang/649/huyen-chau-thanh-a.html',
# '/hau-giang/652/huyen-vi-thuy.html',
# '/hau-giang/707/thi-xa-long-my.html',
# '/hau-giang/650/huyen-long-my.html',
# '/hau-giang/647/thi-xa-nga-bay.html',
# '/hau-giang/646/thanh-pho-vi-thanh.html',
# '/hau-giang/648/huyen-chau-thanh.html',
# '/hau-giang/651/huyen-phung-hiep.html',


# https://alonhadat.com.vn/nha-dat/can-ban/dat-tho-cu-dat-o/hau-giang/651/huyen-phung-hiep.html

# https://alonhadat.com.vn/nha-dat/can-ban/nha-mat-tien/29/hau-giang.html
# https://alonhadat.com.vn/nha-dat/can-ban/nha-trong-hem/hau-giang/652/huyen-vi-thuy.html

wards=[
    '/hau-giang/649/huyen-chau-thanh-a.html',
    '/hau-giang/652/huyen-vi-thuy.html',
    '/hau-giang/707/thi-xa-long-my.html',
    '/hau-giang/650/huyen-long-my.html',
    '/hau-giang/647/thi-xa-nga-bay.html',
    '/hau-giang/646/thanh-pho-vi-thanh.html',
    '/hau-giang/648/huyen-chau-thanh.html',
    '/hau-giang/651/huyen-phung-hiep.html',
]
types=[
    'dat-tho-cu-dat-o',
    'nha-mat-tien',
    'nha-trong-hem'
]
data_table = []
for ward in wards:
    for type in types:
        page = requests.get("https://alonhadat.com.vn/nha-dat/can-ban/"+type+ward)

        soup = BeautifulSoup(page.content, 'html.parser')
        week = soup.find(class_='content-items')

        items = soup.find_all(class_='content-item')
        for item in items:
            price = item.find(class_='ct_price').get_text()
            dt = item.find(class_='ct_dt').get_text()
            dis = item.find(class_='ct_dis').get_text()
            data_table.append({'price': price,
                                'dt': dt,
                                'dis': dis,
                                'type': type,
                                'ward': ward})

dataframe = pd.DataFrame(data=data_table)
print(dataframe)
dataframe.to_excel("alonhadat_haugiang.xlsx", engine='xlsxwriter')