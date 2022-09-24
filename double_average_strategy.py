import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

# 设置显示所有列
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

# 读取合约信息数据
path = "D:\code\SRP_test\主力合约资料 2022-09-06 15-16\主力合约资料 2022-09-06 15-16CFFEX.IC.csv"
df = pd.read_csv(path)
print(df.head(30))
# print(len(df))

# print(df.head(30))
# 生成长短周期的均值并加在df对象中
# 参数设置：长短周期的具体小时数
short_cycle_hours = 12
long_cycle_hours = 26
# 具体生成均值代码
df['short_cycle'] = np.nan
df['long_cycle'] = np.nan
for i in range(short_cycle_hours-1,len(df)):
    df.loc[df.index[i],'short_cycle'] = df.loc[df.index[i-short_cycle_hours-1:i+1],'open'].mean()
for i in range(long_cycle_hours-1,len(df)):
    df.loc[df.index[i],'long_cycle'] = df.loc[df.index[i-long_cycle_hours-1:i+1],'open'].mean()
# print(df.head(30))

# 根据双均线策略生成金叉和死叉
# golden_cross 和 death_cross 内存放的是金叉和死叉的行号
df = df.dropna()
golden_cross = []
death_cross = []
for i in range(long_cycle_hours+2,len(df)):
    if df['short_cycle'][i] >= df['long_cycle'][i] and df['short_cycle'][i-1] < df['long_cycle'][i-1]:
        golden_cross.append(df.index[i])
    if df['short_cycle'][i] <= df['long_cycle'][i] and df['short_cycle'][i-1] > df['long_cycle'][i-1]:
        death_cross.append(df.index[i])
print(golden_cross)
print(death_cross)