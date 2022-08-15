# Author:阿楠&花北猫
# -*- codeing = utf-8 -*-
# @Time:2022/8/11 21:07
import json

import requests

'''
请求accessToken
url = 'https://open.ys7.com/api/lapp/token/get'
head = {
    'Host':'open.ys7.com',
    'Content-Type':'application/x-www-form-urlencoded',
}
data = {
    'appKey':'b95b5fff375b46478dd0ea98ecdae45c',
    'appSecret':'21dd28d816cb7f8dda8e253197f15ac2'
}
json_data = json.dumps(data)

req = requests.post(url=url,headers=head,data=data)
print(req.text)


'''


'''
请求摄像头列表
url = 'https://open.ys7.com/api/lapp/camera/list'
head = {
    'Host':'open.ys7.com',
    'Content-Type':'application/x-www-form-urlencoded',
}
data = {
    'accessToken':'at.a9raoo369ul4o3t737ghlb0r9asn9flq-3gnir57da4-1p4isf6-lr0ew2rpt',
}
json_data = json.dumps(data)

req = requests.post(url=url,headers=head,data=data)
print(req.text)


'''


'''
获取流地址
url = 'https://open.ys7.com/api/lapp/v2/live/address/get'
head = {
    'Host':'open.ys7.com',
    'Content-Type':'application/x-www-form-urlencoded',
}
data = {
    'accessToken':'at.a9raoo369ul4o3t737ghlb0r9asn9flq-3gnir57da4-1p4isf6-lr0ew2rpt',
    'deviceSerial':'239631425',
    'protocol':3,
    'expireTime':30000
}
json_data = json.dumps(data)

req = requests.post(url=url,headers=head,data=data)
print(req.text)


'''
'''
class defmethod:

    def get_token(self,appKey,appSecret):
        url = 'https://open.ys7.com/api/lapp/token/get'
        head = {
            'Host': 'open.ys7.com',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'appKey': appKey,
            'appSecret': appSecret
        }
        json_data = json.dumps(data)

        req = requests.post(url=url, headers=head, data=data)
        print(req.text)

d = defmethod
a = 'b95b5fff375b46478dd0ea98ecdae45c'
b = '21dd28d816cb7f8dda8e253197f15ac2'
defmethod.get_token(self=d,appKey=a,appSecret=b)


'''
