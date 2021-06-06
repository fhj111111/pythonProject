import requests
import codecs

# url = 'https://www.lmonkey.com/'
url = 'https://www.kuaidaili.com/free/'
# url = 'https://www.kuaidaili.com/free/intr/'

# 定义请求头信息
headers1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
res = requests.get(url=url,headers=headers1)
# 获取响应状态码

code = res.status_code
print(code)

# 响应成功后响应内容写入文件中

if code == 200:
    with codecs.open('./test.html','w','utf-8')as fp:
        fp.write(res.text)