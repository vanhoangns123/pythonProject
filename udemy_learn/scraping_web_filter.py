import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import urllib.request, json 

parsed_json = {}
with urllib.request.urlopen("https://gateway.chotot.com/v1/public/web-proxy-api/loadRegions") as url:
    parsed_json = json.loads(url.read())


# Export Region_area_data VietNam
data_table = []
regions = parsed_json['regionFollowId']['entities']['regions']
for region in regions.values():
    region_name = region['name']
    region_id = region['id']

    for area in region['area'].values():
        area_name = area['name']
        area_id = area['id']

        data_table.append({'region_name': region_name, 
                            'region_id' : region_id, 
                            'area_name' : area_name,
                            'area_id'   : area_id})

dataframe = pd.DataFrame(data=data_table)
dataframe.to_excel("region_area_data.xlsx", engine='xlsxwriter')

