from tqsdk import TqApi, TqAuth, TqAccount, TargetPosTask

# from tqsdk import TqApi, TqAuth

#创建API实例,传入自己的信易账户
api = TqApi(auth=TqAuth("lievan", "kuaiqi0910"))

# 获得中金所 IF主力 的行情引用，当行情有变化时 quote 中的字段会对应更新
quote = api.get_quote("CFFEX.IF2107")

# 输出 IF主力 的最新行情时间和最新价
print(quote.datetime, quote.last_price)

# 关闭api,释放资源
api.close()
api = TqApi(TqAccount("H海通期货", "4003242", "123456"), auth=TqAuth("lievan", "kuaiqi0910"))  # 创建 TqApi 实例, 指定交易账户
q_1910 = api.get_quote("SHFE.rb1910")  # 订阅近月合约行情
t_1910 = TargetPosTask(api, "SHFE.rb1910")  # 创建近月合约调仓工具
q_2001 = api.get_quote("SHFE.rb2001")  # 订阅远月合约行情
t_2001 = TargetPosTask(api, "SHFE.rb2001")  # 创建远月合约调仓工具

while True:
    api.wait_update()  # 等待数据更新
    spread = q_1910["last_price"] - q_2001["last_price"]  # 计算近月合约-远月合约价差
    print("当前价差:", spread)
    if spread > 250:
        print("价差过高: 空近月，多远月")
        t_1910.set_target_volume(-1)  # 要求把1910合约调整为空头1手
        t_2001.set_target_volume(1)  # 要求把2001合约调整为多头1手
    elif spread < 200:
        print("价差回复: 清空持仓")  # 要求把 1910 和 2001合约都调整为不持仓
        t_1910.set_target_volume(0)
        t_2001.set_target_volume(0)
