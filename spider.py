import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

# now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
# filename = r'主力合约资料 '+now+'.csv'
# url = 'http://hotmap.icetech.com.cn/hotmap.html'
class spider:
    def __init__(self):
        self.now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
        self.filename = r'主力合约资料 ' + self.now + '.csv'
        self.url = 'http://hotmap.icetech.com.cn/hotmap.html'
        self.html = urlopen(self.url)
        self.bsObj = BeautifulSoup(self.html,"html.parser")
        self.table = self.bsObj.findAll("table")[0]
    def start_spider(self):
        if self.table is None:
            print("no table")
            exit(1)
        rows = self.table.findAll("tr")
        csvFile = open(self.filename,'wt',newline='',encoding='gbk')
        writer = csv.writer(csvFile)
        try:
            for row in rows:
                csvRow = []
                cnt = 0
                for cell in row.findAll(['td','th']):
                    cnt+=1
                    if cnt==4 or cnt==5:continue
                    csvRow.append(cell.get_text())
                if csvRow[-1] and csvRow[-1]!="ChangeToMonth":
                    csvRow[-2] = csvRow[-1][-6:]
                if csvRow[-1]=="ChangeToMonth":
                    csvRow.append("Symbol")
                    csvRow.append("Id")
                else:
                    csvRow.append(csvRow[0]+'.'+csvRow[1])
                    csvRow.append(csvRow[0]+'.'+csvRow[1]+csvRow[3])
                writer.writerow(csvRow)
            # writer.writerow([11])
        finally:
            csvFile.close()