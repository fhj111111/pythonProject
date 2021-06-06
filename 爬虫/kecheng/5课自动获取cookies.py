import requests

url = "http://127.0.0.1:3000/api/user/login"

payload="{\"email\":\"admin@admin.com\",\"password\":\"admin\"}"
headers = {
  'Cookie': '_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjExLCJpYXQiOjE2MTcxMjIxNjUsImV4cCI6MTYxNzcyNjk2NX0.1X7ta8OO8rsqz_tNUMQbWyqqohco_tOY2nNptuvByts; _yapi_uid=11; _yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjExLCJpYXQiOjE2MjAzMDkxOTcsImV4cCI6MTYyMDkxMzk5N30.ET62ffP3y9xFK1_aECLMxaLYb_gxzEgEWLkEbbc0PE4; _yapi_uid=11',
  'Content-Type': 'application/json'
}

req = requests.Session()
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)


url1 = 'http://127.0.0.1:3000/group/11'
res = req.get(url=url1,headers=headers)
print(res.text)
# res = requests.request("GET",url=url,headers=hed)
