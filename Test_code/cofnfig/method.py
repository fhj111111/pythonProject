import requests
import json


class RunMetdoh:

    def __init__(self, url=None, method=None, heasers=None, data=None):
        self.url = url
        self.method = method
        self.heasers = heasers
        self.data = data

    def send_get(self, method, url, data, headers):
        res = requests.request(method, url=url, headers=headers)
        return res.json()

    def send_post(self, method, url, data):
        res = requests.request(method, url=url, data=data)
        return res.json()

    def run_main(self, method=None, url=None, data=None, headers=None):
        if method == 'post':
            res = self.send_post(method, url, data)
            # # return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)
            # return json.dumps(res)
        else:
            res = self.send_get(method, url, headers, data)
            # return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)
        return json.dumps(res)