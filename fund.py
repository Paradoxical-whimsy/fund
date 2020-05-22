#导入requests库
import requests
#导入re库
import re

#定义网址变量
url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2019-05-22&ed=2020-05-22&qdii=&tabSubtype=,,,,,&pi={}&pn=50&dx=1'

#定义请求头
header = {}

#定义请求头内容的字符串
s = '''Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
Connection: keep-alive
Cookie: searchbar_code=161726; qgqp_b_id=5644c99a877815eaa2d21ac1dddd8637; cowminicookie=true; intellpositionL=80%25; intellpositionT=656px; st_si=90640908928289; st_asi=delete; ASP.NET_SessionId=v5g2ppwo1yi40k2lawlfdzif; st_pvi=63444169218271; st_sp=2020-01-20%2023%3A37%3A16; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=3; st_psi=20200522204019144-112200304021-9968676370
Host: fund.eastmoney.com
Referer: http://fund.eastmoney.com/data/fundranking.html
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'''

#把字符串的内容存入请求头
for line in s.split('\n'):
    header[line.split(': ')[0]] = line.split(': ')[1]

#定义存放数据的列表
funds = []

#定义最大页数
MAX_PAGE = 120

#获取数据
for page in range(1, MAX_PAGE + 1):
    #格式化url后获取该页数据
    res = requests.get(url.format(page), headers=header)
    #把获取的数据加到funds里
    datas = eval(re.findall('\[.*?\]', res.text, re.S)[0])
    for data in datas:
        funds.append(data)

    print(page)

#把数据保存为文件
with open('funds.csv', 'w', encoding='gbk') as f:
    #写入表头
    f.write('基金代码,基金名字,名字缩写,日期,单位净值,累计净值,日增长率,近一周,近1月,近3月,近6月,近1年,近2年,近3年,今年来,成立来,成立日,买入后锁定期,自定义,原费率,手续费,折扣,手续费,折扣,不知道\n')
    for fund in funds:
        f.write(fund + '\n')
