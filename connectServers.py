# -*- coding: utf-8 -*-
import paramiko,sys,multiprocessing.managers,os
from testerDatabase import Common
from configparser import ConfigParser



#1：连接被打压机器
#2：连接打压机器，打开master和slave
#3：先执行slave，后master



class Test:
    def connect_server(self,host: str, port=22, username="root", password="123456", client=100, request=10, runtime=30,
                       cacheEnable=None, servername=None, serverhosts=None, httptype=None, testNum=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        result = []
        try:
            if host == "192.168.0.97":
                stdin, stdout, stderr = ssh.exec_command(
                    'cd /home/ssm/project/TL.PressureTest && ./Run_master_locust.sh {0} {1} {2} {3} {4} {5} {6} {7}'.format(
                        client, request, runtime, cacheEnable, servername, serverhosts, httptype, testNum))

                # 错误提示
                sterr = stderr.read().decode()
                print(sterr)
                # 获取结果
                std = stdout.read().decode()
                print(std)
                result.append(std)


                # stin = stdin.read().decode()
                # print(stin)
                # ssh.close()
            elif host == "192.168.1.171":
                stdin, stdout, stderr = ssh.exec_command(
                    "cd /root/TL.PressureTest && git pull && python login.py && ./Run_slave_locust.sh {0} {1} {2} {3} {4} {5} {6} {7}".format(
                        client, request, runtime, cacheEnable, servername, serverhosts, httptype, testNum))
                # 获取结果
                std = stdout.read().decode()
                #print(result)
                # 错误提示
                err1 = stderr.read().decode()
                print(err1)
                # if err1:
                # print("执行shell错误：",err1)
                # ssh.close()
        except Exception as e:
            print(e)
        return result





# def kill_process(host:str,port=22,username="root",password="123456"):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host, port, username, password)
#     if host=='192.168.0.97':
#         stdin, stdout, stderr = ssh.exec_command("lsof -i:5557 | grep -v PID| awk '{print $2}' | xargs kill")
#         result = stdout.read().decode()
#         print(result)
#         err = stderr.read().decode()
#         if err:
#             print("执行shell错误：", err)
#         ssh.close()
#     if host=='192.168.1.174':
#         stdin, stdout, stderr = ssh.exec_command("ps -aux | grep locust | grep -v 'grep' | awk '{print $2}' |xargs kill")
#         result1 = stdout.read().decode()
#         print(result1)
#         # 错误提示
#         err1 = stderr.read().decode()
#         if err1:
#             print("执行shell错误：",err1)
#         ssh.close()



class GetRet():
    def __init__(self):
        self.result = []
    def add(self,ret):
        self.result.append(ret)
    def get(self):
        return self.result


if __name__ =="__main__":

    cacheEnable = os.getenv("CacheEnable", 'True')
    servername  = os.getenv("ServerName","User")
    serverhosts = os.getenv("serverhosts", "192.168.1.157")
    httptype = os.getenv('Httptype', 'Http_msgpack')
    testNum = int(os.getenv("testNum", '0'))
    client = int(os.getenv('client', "100"))
    request = int(os.getenv('request', "10"))
    runtime = int(os.getenv('runtime', "40"))
    print(cacheEnable,servername,serverhosts,client,request,runtime)
    #从配置文件取数据
    cp = ConfigParser()
    cp.read("conf.ini")
    section = cp.sections()[1]
    count = cp.getint(section, "count")
    publicCount = cp.getint(section, 'publicCount')

    com = Common()
    #清数据
    com.deleteDatabase()
    #公共数据
    com.insert_public_data(create_time='false', count = publicCount,t=None)
    #获取公共数据计数
    co = com.waitfor(timeout = 60*30,interval = 5)
    if co:
        test = Test()
        tasks = multiprocessing.Pool(2)
        task_ctx = [{"host": "192.168.0.97", "user": "ssm", "pwd": "123", "port": 22},
                    {"host": "192.168.1.171", "user": "root", "pwd": "123456", "port": 22}]
        ret = GetRet()
        for ctx in task_ctx:
            tasks.apply_async(test.connect_server,
                              args=(ctx.get('host'), ctx.get('port'), ctx.get('user'), ctx.get('pwd'),
                                    client, request, runtime, cacheEnable, servername, serverhosts, httptype, testNum,),
                              callback=ret.add)

        tasks.close()
        tasks.join()

        reportdata = ret.get()[1][0]
        if '平均响应时间不符合标准(误差+-100)' in reportdata or '吞吐量不符合标准(误差+-50)' in reportdata:
            sys.exit(1)








