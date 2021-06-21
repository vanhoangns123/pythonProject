import pandas as pd
import urllib.request, json 

class ExcelPython:
    def __init__(self, fileName):
        self.df = pd.read_excel ('./'+fileName+'.xlsx') 
        self.fileName = fileName

        self.numRow = self.df.shape[0]
        self.numCol = self.df.shape[1]

    def getAreaAverage(self, porperty_type):
        df = self.df.filter(['area_id'], axis=1)
        price = []
        ward_count = []
        avarage = []

        # group areaid & sum price
        for i in range(self.numRow):
            item_price = self.df[porperty_type][i]
            count = 1
            if(item_price == "empty"):
                item_price = 0
                count = 0
            price.append(int(item_price))
            ward_count.append(count)
        
        df['price'] = price
        df['ward_count'] = ward_count
        g = df.groupby('area_id', as_index=False, sort=False).sum()

        # calculate avarage price
        for i in range(g.shape[0]):
            avr = 0
            if (g['price'][i] != 0):
                avr = g['price'][i] / g['ward_count'][i]
            avarage.append(round(avr))

        g['avarage'] = avarage

        # add avarage value & check if valid
        self.addAreaAveragePrice(g, porperty_type)


    def addAreaAveragePrice(self, averageAreaDf, porperty_type):
        df = self.df
        data = []
        data_err = []

        group = 0
        for i in range(self.numRow):
            # add avarage value
            if (int(df['area_id'][i]) != averageAreaDf['area_id'][group]):
                group = group + 1
            data.append(averageAreaDf['avarage'][group])

            # check if valid value
            dif = 0
            if (df[porperty_type][i] != "empty"):
                sub = abs(int(df[porperty_type][i]) - averageAreaDf['avarage'][group])
                avr = (int(df[porperty_type][i]) + averageAreaDf['avarage'][group])/2
                dif = sub/avr
            
            if(dif >= 0.5):
                data_err.append(1)
            else:
                data_err.append(0)

        self.df[porperty_type+"_avr"]=data
        self.df[porperty_type+"_err"]=data_err

    def Average(lst):
        return sum(lst) / len(lst)

    def export(self):
        self.df.to_excel("./" + self.fileName + '_exported.xlsx', index=False);


excelFile = ExcelPython('final_scraping_file')
excelFile.getAreaAverage('dat')
excelFile.getAreaAverage('nha_o')
excelFile.getAreaAverage('can_ho')
excelFile.getAreaAverage('van_phong')
excelFile.export()