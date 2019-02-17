# -*- coding: utf-8 -*-
from locust.clients import HttpSession
import json,os,msgpack
from filter_null import ins_filter
from configparser import ConfigParser



cp = ConfigParser()
cp.read("conf.ini")
section = cp.sections()[2]
serverhosts = cp.get(section, 'serverhosts')

basehost = os.getenv("serverhosts",serverhosts)
base = "http://"+basehost
base_api_url = base+ ":8096"



#json 格式
class Http_json:
    @staticmethod
    def get(port,url,au):
        http = HttpSession(base+":"+port)
        data = http.get(url,headers={'Authorization': au, 'Content-Type': 'application/json',
                                               'accept': 'application/json'})
        return data

    @staticmethod
    def post(port,url, data, au):
        http = HttpSession(base+":"+port)
        data = http.post(url, data=json.dumps(data), headers={'Authorization': au, 'Content-Type': 'application/json',
                                                 'accept': 'application/json'})
        return data

    @staticmethod
    def put(port,url, data, au):
        http = HttpSession(base + ":" + port)
        data = http.put(url, data=json.dumps(data), headers={'Authorization': au, 'Content-Type': 'application/json',
                                                'accept': 'application/json'})
        return data

    @staticmethod
    def delete(port,url, au):
        http = HttpSession(base + ":" + port)
        data = http.delete(url, headers={'Authorization': au, 'Content-Type': 'application/json',
                                             'accept': 'application/json'})
        return data

#msgpack 格式
class Http_esponseDecode:
    #@staticmethod
    def __init__(self,response_data):
        # 其实这个_dict就已经是一个json了
        _dict = msgpack.unpackb(response_data.content, encoding="utf8")
        _dict = ins_filter.filter_null(_dict)
        #单引号换成双引号，双引号加上转义。，None换成null
        self.text = json.dumps(_dict) #.replace('"', '\"').replace("'", '"').replace(' None', ' null')
        self.status_code = response_data.status_code


class Http_msgpack:
    @staticmethod
    def get(port,url, au):
        # data = requests.get(url, data, headers={'Authorization': au, 'Content-Type': 'application/json',
        #                                         'accept': 'application/msgpack'})
        http = HttpSession(base + ":" + port)
        data = http.get(url, headers={'Authorization': au, 'Content-Type': 'application/json',
                                      'accept': 'application/msgpack'})
        if data.status_code == 204:
            return data
        elif data.content == b'': #返回值为空
            return data
        else:
            return Http_esponseDecode(data)

    @staticmethod
    def post(port,url, data, au):
        # data = requests.post(url, data, headers={'Authorization': au, 'Content-Type': 'application/json',
        #                                          'accept': 'application/msgpack'})
        http = HttpSession(base + ":" + port)
        data = http.post(url, data=json.dumps(data), headers={'Authorization': au, 'Content-Type': 'application/json',
                                                              'accept': 'application/msgpack'})
        #return msgpack.unpackb(data.content, encoding="utf8")
        if data.status_code == 204:
            return data
        elif data.content == b'': #返回值为空
            return data
        else:
            return Http_esponseDecode(data)

    @staticmethod
    def put(port,url, data, au):
        # data = requests.put(url, data, headers={'Authorization': au, 'Content-Type': 'application/json',
        #                                         'accept': 'application/msgpack'})
        http = HttpSession(base + ":" + port)
        data = http.put(url, data=json.dumps(data), headers={'Authorization': au, 'Content-Type': 'application/json',
                                                             'accept': 'application/msgpack'})
        if data.status_code == 204:
            return data
        elif data.content == b'': #返回值为空
            return data
        else:
            return Http_esponseDecode(data)

    @staticmethod
    def delete(port,url, au):
        # data = requests.delete(url, data=data, headers={'Authorization': au, 'Content-Type': 'application/json',
        #                                      'accept': 'application/msgpack'})
        http = HttpSession(base + ":" + port)
        data = http.delete(url, headers={'Authorization': au, 'Content-Type': 'application/json',
                                         'accept': 'application/msgpack'})
        if data.status_code == 400:
            return Http_esponseDecode(data)
        else:
            return data





