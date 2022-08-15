# Author:阿楠&花北猫
# -*- codeing = utf-8 -*-
# @Time:2022/8/12 9:22
import requests
import json


class defmethod:
    '''获取a模式下子账号token'''
    def get_a_token(self,accountId):
        try:
            url = 'https://dw.yukongiot.com/api/ys7/getAccessToken?accountId=2377b6c5c00940919fdaeb9feb537922'

            req = requests.get(url=url)
            return req
        except:
            print('这里错了')
            msg = {
                'msg': '获取atoken请求失败'
            }
            return msg

    '''获取b模式下子账号token'''
    def get_b_token(self,accessToken,accountId):
        try:
            url = 'https://open.ys7.com/api/lapp/ram/token/get'
            head = {
                'Host': 'open.ys7.com',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            data = {
                'accessToken': accessToken,
                'accountId': accountId
            }
            json_data = json.dumps(data)

            req = requests.post(url=url, headers=head, data=data)
            return req
        except:
            print('这里错了')
            msg = {
                'msg': '获取token请求失败'
            }
            return msg




    '''获取主账号token信息'''
    def get_token(self,appKey,appSecret):
        try:
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
            return req
        except:
            print('这里错了')
            msg = {
                'msg':'获取token请求失败'
            }
            return msg
    '''获取摄像头列表'''
    def get_list(self,accessToken,pageStart,pageSize):
        try:
            url = 'https://open.ys7.com/api/lapp/camera/list'
            head = {
                'Host': 'open.ys7.com',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            data = {
                'accessToken': accessToken,
                'pageStart':pageStart,
                'pageSize':pageSize
            }
            json_data = json.dumps(data)

            req = requests.post(url=url, headers=head, data=data)
            return  req
        except:
            list_msg = {
                'list_msg':'获取列表模块错误'
            }
            return list_msg



    '''获取视频流'''
    def get_play(self,accessToken,deviceSerial,protocol):
        try:
            url = 'https://open.ys7.com/api/lapp/v2/live/address/get'
            head = {
                'Host': 'open.ys7.com',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            data = {
                'accessToken': 'at.a9raoo369ul4o3t737ghlb0r9asn9flq-3gnir57da4-1p4isf6-lr0ew2rpt',
                'deviceSerial': '239631425',
                'protocol': 3,
                'expireTime': 30000
            }
            json_data = json.dumps(data)

            req = requests.post(url=url, headers=head, data=data)
            return req
        except:
            play_msg = {
                'play_msg':'播放模块出现错误'
            }
            return play_msg