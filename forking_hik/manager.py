# Author:阿楠&花北猫
# -*- codeing = utf-8 -*-
# @Time:2022/8/11 22:47
import json
from flask import Flask, render_template, request
from some_method import  defmethod


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

'''获取固定的token'''
@app.route('/api/v1/logina/',methods=['GET'])
def get_a_token():
    if request.method == 'GET':
        try:
            d_a_token = defmethod
            str = '2377b6c5c00940919fdaeb9feb537922'
            token_dict = defmethod.get_a_token(self=d_a_token,accountId=str)
            return token_dict.json()
        except:
            msg_token = {
                'msg_token':'获取出错'
            }
            return msg_token



'''获取子账号在b模式下的acessstoken'''
@app.route('/api/v1/loginb/',methods=['GET'])
def get_b_token():
    if request.method == 'GET':
        try:
            d_b_token = defmethod
            accessToken = request.args.get('accessToken')
            accountId = request.args.get('accountId')
            token_dict = defmethod.get_token(self=d_b_token,accessToken=accessToken,accountId=accountId)
            return token_dict.json()
        except:
            msg_token = {
                'msg_token':'获取出错'
            }
            return msg_token.json()




'''获取accessToken'''
@app.route('/api/v1/login/',methods=['GET'])
def get_token():
    if request.method == 'GET':
        try:
            d_token = defmethod
            appKey = request.args.get('appKey')
            appSecret = request.args.get('appSecret')
            token_dict = defmethod.get_token(self=d_token,appKey=appKey,appSecret=appSecret)
            return token_dict.json()
        except:
            msg_token = {
                'msg_token':'获取出错'
            }
            return msg_token.json()


'''获取账号下摄像头列表'''
@app.route('/api/v1/device/list/',methods=['GET'])
def get_list():
    if request.method == 'GET':
        try:
            d_list = defmethod
            accessToken = request.args.get('accessToken')
            pageStart = request.args.get('pageStart')#分页起始页，从0开始  int
            pageSize = request.args.get('pageSize')#分页大小，默认为10，最大为50	 int
            list_dict  = defmethod.get_list(self=d_list,accessToken=accessToken,pageStart=pageStart,pageSize=pageSize)
            return list_dict.json()
        except:
            list_msg = {
                'list_msg':'获取列表模块失效'
            }
            return list_msg.json()


'''获取播放地址'''
@app.route('/api/v1/stream/start/',methods=['GET'])
def get_play():
    if request.method == 'GET':
        try:
            d_play = defmethod
            accessToken = request.args.get('accessToken') #授权过程获取的access_token
            deviceSerial = request.args.get('deviceSerial')  #设备序列号例如427734222，均采用英文符号，限制50个
            protocol = request.args.get('protocol')  #流播放协议，1-ezopen、2-hls、3-rtmp、4-flv，默认为1
            play_dict = defmethod.get_play(self=d_play,accessToken=accessToken,deviceSerial=deviceSerial,protocol=protocol)
            return play_dict.json()
        except:
            play_msg = {
                'play_msg':'获取流错误'
            }




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=30499)