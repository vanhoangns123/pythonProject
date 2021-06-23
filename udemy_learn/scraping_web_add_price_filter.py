import pandas as pd
import urllib.request, json 
import ast

def Average(lst):
    return sum(lst) / len(lst)
class ExcelPython:
    def __init__(self, fileName, filterList = []):
        self.df = pd.read_excel ('./'+fileName+'.xlsx') 
        self.fileName = fileName
        self.numRow = self.df.shape[0]
        self.numCol = self.df.shape[1]
        self.filterList = filterList

    def getPropertyID(self, propertyName):
        switcher = {
            "dat": 1040,
            "nha_o": 1020,
            "can_ho": 1010,
            "van_phong": 1030
        }
        return switcher.get(propertyName, 1000)

    def getPriceByProperty(self, propertyName, house_type = 0, road_condition = 0):
        df = self.df
        data = []
        data_arr = []

        property_id = self.getPropertyID(propertyName)

        for i in range(self.numRow):
            region_id = list(df['region_id'])[i]
            area_id = list(df['area_id'])[i]
            ward_id = list(df['ward_id'])[i]
            isTotal=""

            if area_id in self.filterList:
                isTotal = "&st=s,k" 

            url_ad = "https://gateway.chotot.com/v1/public/ad-listing?region_v2="+str(region_id)+"&area_v2="+str(area_id)+"&cg="+str(property_id)+"&house_type="+str(house_type)+"&filter_property_road_condition="+str(road_condition)+"&price=1000000000-30000000000&ward="+str(ward_id)+isTotal+"&limit=10&key_param_included=true"
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
            data.append(average)
            data_arr.append(results)

        # Add to df
        housetypeName= ""
        if(house_type == 1 or road_condition == 2):
            housetypeName = "_mat_duong"
        elif(house_type == 3 or road_condition == 1):
            housetypeName = "_ngo_hem"

        self.df[propertyName + housetypeName]=data
        self.df[propertyName + housetypeName+"_arr"]=data_arr

    def getAreaAverage(self, propertyName, propertyPriceArrCol):
        temp = self.createTempAveragePriceDf(propertyName)
        # add avarage value & check if valid
        self.addAreaAveragePrice(temp, propertyName, propertyPriceArrCol)

    def groupCol(self, groupCol, col):
        df = self.df.filter([groupCol, col], axis=1)
        print(df)
        df = df.groupby([groupCol, col], as_index=False, sort=False).size()
        return df

    def groupTable(self, propertyName):
        df = self.df.filter(['area_id'], axis=1)
        price = []
        ward_count = []

        # group areaid & sum price
        for i in range(self.numRow):
            item_price = self.df[propertyName][i]
            count = 1
            if(item_price == "empty"):
                item_price = 0
                count = 0
            price.append(int(item_price))
            ward_count.append(count)
        
        df['price'] = price
        df['ward_count'] = ward_count
        
        tempGroup = df.groupby('area_id', as_index=False, sort=False).sum()
        return tempGroup

    def createTempAveragePriceDf(self, propertyName):
        tempGroup = self.groupTable(propertyName)
        avarage = []
        # calculate avarage price
        for i in range(tempGroup.shape[0]):
            avr = 0
            if (tempGroup['price'][i] != 0):
                avr = tempGroup['price'][i] / tempGroup['ward_count'][i]
            avarage.append(round(avr))

        tempGroup['avarage'] = avarage
        return tempGroup

    def addAreaAveragePrice(self, averageAreaDf, propertyName, propertyPriceArrCol):
        df = self.df
        data = []
        data_err = []
        group = 0
        for i in range(self.numRow):
            err = 0
            dif = 0

            # add avarage value
            if (int(df['area_id'][i]) != averageAreaDf['area_id'][group]):
                group = group + 1
            data.append(averageAreaDf['avarage'][group])

            # check if only one record of Arr Price
            arrPrice = df[propertyPriceArrCol][i]
            arrPrice = ast.literal_eval(arrPrice)
            if(len(arrPrice) <= 2 ):
                err = 1

            # check if valid value and give error
            if(err == 0):
                if (df[propertyName][i] != "empty"):
                    sub = abs(int(df[propertyName][i]) - averageAreaDf['avarage'][group])
                    avr = (int(df[propertyName][i]) + averageAreaDf['avarage'][group])/2
                    dif = sub/avr
                if(dif >= 0.5):
                    err = 1
                else:
                    err = 0

            data_err.append(err)

        self.df[propertyName+"_avr"]=data
        self.df[propertyName+"_err"]=data_err

    def export(self, fileName):
        self.df.to_excel("./" + fileName + '_exported.xlsx', index=False);


filter = [
    12073,
    12074,
    12075,
    12076,
    12077,
    12078,
    12079,
    12080,
    12081,
    12082,
    12121,
    12129,
    13096,
    13097,
    13098,
    13099,
    13100,
    13101,
    13102,
    13103,
    13104,
    13105,
    13106,
    13107,
    13108,
    13109,
    13110,
    13111,
    13112,
]
excelFile = ExcelPython('region_area_data_dat_exported')
# excelFile.getPriceByProperty('dat')
# excelFile.export('region_area_data_dat')

# excelFile.getPriceByProperty('dat', 0, 1)
# excelFile.export('region_area_data_dat_ngo_hem')

# excelFile.getPriceByProperty('dat', 0, 2)
# excelFile.export('region_area_data_dat_mat_duong')

# excelFile.getPriceByProperty('nha_o')
# excelFile.export('region_area_data_nha_o')

# excelFile.getPriceByProperty('nha_o', 3)
# excelFile.export('region_area_data_nha_o_ngo_hem')

# excelFile.getPriceByProperty('nha_o', 1)
# excelFile.export('region_area_data_nha_o_mat_duong')

# excelFile.getPriceByProperty('can_ho')
# excelFile.export('region_area_data_can_ho')

# excelFile.getPriceByProperty('van_phong')
# excelFile.export('region_area_data_van_phong')


excelFile.getAreaAverage('dat', 'dat_arr')
excelFile.getAreaAverage('dat_ngo_hem_ngo_hem', 'dat_ngo_hem_ngo_hem_arr')
excelFile.getAreaAverage('dat_mat_duong_mat_duong', 'dat_mat_duong_mat_duong_arr')
excelFile.getAreaAverage('nha_o', 'nha_o_arr')
excelFile.getAreaAverage('nha_o_mat_duong_mat_duong', 'nha_o_mat_duong_mat_duong_arr')
excelFile.getAreaAverage('nha_o_ngo_hem_ngo_hem', 'nha_o_ngo_hem_ngo_hem_arr')
excelFile.getAreaAverage('van_phong', 'van_phong_arr')
excelFile.getAreaAverage('can_ho', 'can_ho_arr')


excelFile.export('region_area_data_dat_export_done')

# temp = excelFile.groupCol("area_name", "area_id")
# excelFile.export('areaList', temp)

