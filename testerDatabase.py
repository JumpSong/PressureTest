# -*- coding: utf-8 -*-
from configparser import ConfigParser
import requests,time,os

#1:初始化数据,灌数据,获取灌数据计数


basehost = os.getenv("host","192.168.1.157")
base = "http://"+basehost
base_api_url = base+ ":8096"

#从配置文件取数据
cp = ConfigParser()
cp.read("conf.ini")
section = cp.sections()[1]
count = cp.getint(section, "count")
publicCount = cp.getint(section, 'publicCount')



class Common():
    # 初始化数据库
    def deleteDatabase(self):
        obj = requests.delete(base_api_url + '/manager/tester/testservices/database/data')
        Common.out_error(obj)

    # 公共数据
    def insert_public_data(self, create_time='false', count=100000, t=round(time.time())):
        d = {'createTimer': create_time, 'utcTime': t}
        obj = requests.post(
            base_api_url + '/manager/tester/pressuredataservices/public?createTimer={0}&count={1}'.format(
                create_time, count))
        Common.out_error(obj)

    def get_public_count(self):
        obj = requests.get(
            base_api_url + '/manager/tester/pressuredataservices/public/count')
        return int(obj.content)


    # 微网关数据
    def reset_mservice_data(self, mservicename=None, create_time='false', t=round(time.time())):
        d = {'createTimer': create_time, 'utcTime': t}
        obj = requests.post(base_api_url + '/manager/tester/pressuredataservices/{0}'.format(mservicename))
        Common.out_error(obj)

        # 微网关数据

    def get_mservice_count(self, server):
        mServiceName = 'Manager_' + server + 'TesterService'
        obj = requests.get(base_api_url + '/manager/tester/pressuredataservices/{0}/count'.format(mServiceName))
        return int(obj.content)

    @staticmethod
    def out_error(o):
        if o.status_code != 200:
            print('请求失败' + str(o.status_code) + o.url)
            print(o.text)
            raise Exception(o.text)

    def insert_mservice_data(self,server):
        mServiceName = 'Manager_'+server+'TesterService'
        self.reset_mservice_data(mservicename=mServiceName, create_time='false', t=None)
        time.sleep(30)

    def cache(self,cacheEnable):
        obj = requests.delete(base_api_url + '/manager/tester/testservices/database/memcache/data?enable={0}'.format(cacheEnable))
        Common.out_error(obj)


    #公共数据统计轮询
    def waitfor(self,timeout = 600,interval = 5):
        starttime = time.time()
        while True:
            count = Common.get_public_count(self)
            if  count == publicCount:
                return True
            else:
                runtime = time.time()-starttime
                if runtime>=timeout:
                    print("---------获取公共数据超时---------")
                    raise Exception
                time.sleep(interval)

    # 微网关数据统计轮询
    def waitformservice(self, timeout=60*3, interval=5,server=None):
        starttime = time.time()
        while True:
            count = Common.get_mservice_count(self,server)
            if count == publicCount:
                return True
            else:
                runtime = time.time() - starttime
                if runtime >= timeout:
                    print("---------获取微网关数据超时---------")
                    raise Exception
                time.sleep(interval)

