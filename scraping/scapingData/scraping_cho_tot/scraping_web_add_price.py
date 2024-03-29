import pandas as pd
import urllib.request, json 

df = pd.read_excel ('./YourNewExcel.xlsx') 
count_row = df.shape[0]

property_type = 1030
van_phong = []
van_phong_arr = []


def Average(lst):
    return sum(lst) / len(lst)

for i in range(count_row):
    region_id = list(df['region_id'])[i]
    area_id = list(df['area_id'])[i]
    ward_id = list(df['ward_id'])[i]

    url_ad = "https://gateway.chotot.com/v1/public/ad-listing?region_v2="+str(region_id)+"&area_v2="+str(area_id)+"&cg="+str(property_type)+"&price=1000000000-30000000000&ward="+str(ward_id)+"&st=s,k&limit=20&key_param_included=true"
    temp_data = []
    results = []

    print("Scraping Ward " + str(ward_id) + " | row " + str(i) + " :"+ url_ad)
    with urllib.request.urlopen(url_ad) as url:
        temp_data = json.loads(url.read())

    # Price
    for ad in temp_data['ads']:
        if "size" in ad and "price" in ad:
            size = ad['size']
            price = ad['price']
            rs = round(price/size)
            results.append(rs)
            

    # Avarange
    if len(results) > 0:
        average = Average(results)
    else:
        average = "empty"

    # Append
    van_phong.append(average)
    van_phong_arr.append(results)


df['van_phong'] = pd.Series(van_phong)
df['van_phong_arr'] = pd.Series(van_phong_arr)
df.to_excel("./YourNewExcel.xlsx", index=False);
