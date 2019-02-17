# -*- coding: utf-8 -*-
from locust.clients import HttpSession
import Database
import json,os,time
from configparser import ConfigParser


#1：登陆获取令牌并写入到txt文件


cp = ConfigParser()
cp.read("conf.ini")
section = cp.sections()[2]
serverhosts = cp.get(section, 'serverhosts')
K8sServer = cp.get(section,'K8sServer')

class loginCommon():

    hostster = K8sServer.split('192.168.1.')[1]


    #获取手机号
    def get_mobile(self,count)->list:
        mobiles = list()
        # for m in range(0,count):
        #     Mobile = (Database.OperationDb_interface('mysql'+self.hostster+'_user').selectOne(
        #         "select mobile from tbsoul limit {0},1".format(m))).get('mobile')  # 从数据库取第一条数据
        #     mobiles.append(Mobile)  # 获取键为mobile的值
        Mobile = (Database.OperationDb_interface('mysql' + self.hostster + '_user').selectAll(
                 "select mobile from tbsoul limit {0}".format(count)))
        [mobiles.append(i.get('mobile')) for i in Mobile]
        return mobiles

    #登录,获取令牌，work,love,life用户
    def test_token_work(self,count):
        mobiles =self.get_mobile(count)
        Worktoken = list()
        Lovetoken = list()
        lifetoken = list()
        url = "http://"+K8sServer+":10001"
        t = HttpSession(url)
        header = {"Content-Type": "application/json"}
        for i in mobiles:
            data = {"Uid": "string", "DeviceName": "string", "Lat": 0, "Lon": 0, "Mobile": i, "Password": 123456}
            obj = t.post('/v1/logins/users', data=json.dumps(data), headers=header)
            WorkAuthorization = json.loads(obj.text).get('WorkAuthorization')
            if WorkAuthorization:
                Worktoken.append(WorkAuthorization)
                Worktoken.append('\n')
            LoveAuthorization = json.loads(obj.text).get('LoveAuthorization')
            if LoveAuthorization:
                Lovetoken.append(LoveAuthorization)
                Lovetoken.append('\n')
            LifeAuthorization = json.loads(obj.text).get('LifeAuthorization')
            if  LoveAuthorization:
                lifetoken.append(LifeAuthorization)
                lifetoken.append('\n')

        with open('token/WorkAuthorization.txt', 'w') as f:
            f.writelines(Worktoken)

        with open('token/LoveAuthorization.txt','w') as l:
            l.writelines(Lovetoken)

        with open('token/LifeAuthorization.txt', 'w') as i:
            i.writelines(lifetoken)





if __name__ == "__main__":
    #从配置文件取数据
    cp = ConfigParser()
    cp.read("conf.ini")
    section = cp.sections()[1]
    count = cp.getint(section, "logincount")
    #实例化
    common = loginCommon()
    #登陆
    common.test_token_work(count)







