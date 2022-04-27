# Automatic-quantitative-transaction-based-on-Python-SRP-



# 一句话用法

- 只需运行 **get_main_contract_data** 即可以

- 会自动生成带有当前年月日时分的主力合约文件夹，其中每个csv文件对应一个主力合约

- 每个csv文件含有以下字段
  
  - id 
  
  - 时间 
  
  - 开盘价
  
  - 收盘价
  
  - 最高价
  
  - 最低价
  
  - 交易量



# 更新日志

## 2022.04.28

*****

- 将spider模块封装成类，避免被import之后就运行整体代码

- 完成了 task2 即根据 task1 获取的主力合约名称得到主力合约资料数据

- 