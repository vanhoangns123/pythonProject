import pandas as pd

df = pd.read_excel ('./region_area_data.xlsx') 

# df = pd.DataFrame(data, columns= ['region_name','region_id'])

li = df['ward_id'].tolist()
df['new'] = li

df.to_excel("./YourNewExcel.xlsx", index=False);