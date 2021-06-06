import requests
import xlrd

# 打开excel
file = xlrd.open_workbook('接口用例.xlsx')
print(file.sheet_by_index(0).cell_value(1,2))


url = file.sheet_by_index(0).cell_value(1,2)
data = {'sort': 'desc', 'time': '1418816972', 'key': 'VbyT/YduHtr+iJmL94g2RWzEOwTgsJeZ/pxx6Q	'}

t = requests.get(url=url, params=data)
print(t.text)
print(t.json()['reason'])


url2 = 'http://v.juhe.cn/toutiao/index'
data2 = {'key' : '','type':'社会'}
respoer = requests.post(url=url2,data=data2)


print(respoer.text)
print(respoer.json()['resultcode'])

