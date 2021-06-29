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
    region_geo = region['geo']

    for area in region['area'].values():
        area_name = area['name']
        area_id = area['id']
        area_geo = area['geo']


        #Get Wards
        temp_data = {}
        with urllib.request.urlopen("https://gateway.chotot.com/v2/public/chapy-pro/wards?area="+ area_id) as url:
            temp_data = json.loads(url.read())

        wards = temp_data['wards']
        for ward in wards:
            ward_name = ward['name']
            ward_id = ward['id']

            #Append Dataframe
            data_table.append({'region_name': region_name, 
                                'region_id' : region_id, 
                                'region_geo': region_geo, 
                                'area_name' : area_name,
                                'area_id'   : area_id,
                                'area_geo'  : area_geo,
                                'ward_name' : ward_name,
                                'ward_id'   : ward_id 
                            })

dataframe = pd.DataFrame(data=data_table)

print(dataframe)
dataframe.to_excel("region_area_data.xlsx", engine='xlsxwriter')



