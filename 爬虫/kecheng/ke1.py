import requests

url = 'https://www.baidu.com'

res = requests.get(url)

print(res)
print(res.status_code)
print(res.text)
print(res.url)
print(res.request.headers)
print(res.headers)