import requests

# 请求的url
url = "http://api.fanyi.baidu.com/api/trans/vip/translate"

# 定义请求头

handers = {
"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8"

}

# post 发送的数据
data ={"kw": "nihao"}
# 发送请求

# res = requests.post(url,handers1,data)
res = requests.post(url,handers,data)

# 接受数据
code = res.status_code
if code == 200:
    print('请求成功',data)
    print(code)
    data = res.json()
    if data['error'] == 0:
        print('响应成功')
        k = data['data'][0]['k']
        v = data['data'][0]['v'].spit (';')[-2]
        print(k,'========',v)