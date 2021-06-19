import pandas as pd
import urllib.request, json 

df = pd.read_excel ('./YourNewExcel.xlsx') 
count_row = df.shape[0]

temp_dat = df['dat'].dropna().tolist()


# ward_ids = df['ward_id'].tolist()
# for ward_id in ward_ids:

property_type = 1040
dat = []
dat_arr = []


temp_dat.append('testttt')
dat = temp_dat
# dat_arr = temp_dat_arr.append('testttt')

print(dat)
# print(temp_dat_arr)

def Average(lst):
    return sum(lst) / len(lst)

# for i in range(1000):
#   region_id = list(df['region_id'])[i]
#   area_id = list(df['area_id'])[i]
#   ward_id = list(df['ward_id'])[i]

#   url_ad = "https://gateway.chotot.com/v1/public/ad-listing?region_v2="+str(region_id)+"&area_v2="+str(area_id)+"&cg="+str(property_type)+"&price=1000000000-30000000000&ward="+str(ward_id)+"&st=s,k&limit=20&key_param_included=true"

#   with urllib.request.urlopen(url_ad) as url:
#     temp_data = json.loads(url.read())
    
#     results = []
#     for ad in temp_data['ads']:
#       size = ad['size']
#       price = ad['price']
#       if(price > 0):
#         rs = price/size
#         results.append(rs)
#     if len(results) > 0:
#       average = Average(results)
#     else:
#       average = "empty"
#     dat.append(average)
#     dat_arr.append(results)

df['dat'] = pd.Series(dat)
# df['dat_arr'] = pd.Series(dat_arr)
df.to_excel("./YourNewExcel.xlsx", index=False);

# df['new'] = li
# df.to_excel("./YourNewExcel.xlsx", index=False);
