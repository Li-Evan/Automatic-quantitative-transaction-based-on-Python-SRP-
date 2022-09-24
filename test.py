# import csv
# import pandas as pd
# from spider import spider
#
# spider = spider()
# filename = spider.filename # 生成的文件名
# spider.start_spider() # 爬取
#
# file = pd.read_csv(filename,encoding='gbk')
# for index,row in file.iterrows():
#     print(type(row['Symbol']))
#     print(row['Symbol'])

import os

filename = "1111"
path = './' + filename + '/'  # 想要创建的⽂件
if not os.path.isdir(path):  # 如果 test_data1 该⽂件不存在，就创建该⽂件
    os.mkdir(path)  # 前提是 test_data 这个路径是存在
