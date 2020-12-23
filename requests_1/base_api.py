import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wwfe13234cec58c3dc'
        corpsecret = 'VKsLS3QjroH8ApOBRJry18-g7d3aSn0_7wwPL-7oV8s'
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }

        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r
