from tqsdk import TqApi, TqAuth
from datetime import datetime
import pandas as pd
from spider import spider
import os

spider = spider()
filename = spider.filename
spider.start_spider()  # 爬取

class get_data:
    def __init__(self,filename):
        self.filename = filename
    def get_main_contract_name(self):
        main_contract_list = []
        file = pd.read_csv(self.filename, encoding='gbk')
        for index, row in file.iterrows():
            main_contract_list.append(row['Symbol'])
        return main_contract_list

    def get_single_data(self,name,path):

        api = TqApi(auth=TqAuth("lievan", "kuaiqi0910"))
        my_name = self.filename[:-4]+name+".csv" # 生成的文件名
        print(my_name)
        save_path = os.path.join(path,my_name) # 这样子生成的文件才能保存在指定文件夹下
        # quote = api.get_quote("KQ.m@CFFEX.IC")
        # # 打印现在螺纹钢主连的标的合约
        # print(quote.underlying_symbol)
        quote_str = "KQ.m@"+name
        name_id = api.get_quote(quote_str).underlying_symbol

        klines = api.get_kline_serial(name_id, duration_seconds=60,data_length=930) # 一天有465条线
        klines.loc[:,'id' ] = name_id
        klines['datetime']=klines['datetime'].apply(lambda x:datetime.fromtimestamp(x/1e9))
        cols_to_keep = ['id','datetime','open','high','low','close','volume']
        # id 时间 开盘价、收盘价、最高价、最低价、交易量
        # print(type(klines.loc[:, cols_to_keep]))
        klines.loc[cols_to_keep].to_csv(save_path, index=None)
        # print(klines)
        api.close()

    def get_all_data(self):
        path = './' + self.filename[:-4] + '/'  # 想要创建的⽂件
        if not os.path.isdir(path):  # 如果 path 这个⽂件不存在，就创建该⽂件
            os.mkdir(path)  # 前提是 test_data 这个路径是存在
            print(path)
        name_list = self.get_main_contract_name()
        print(name_list)
        for name in name_list:
            self.get_single_data(name,path)


test=get_data(filename)
test.get_all_data()