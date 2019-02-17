# -*- coding: utf-8 -*-
from locust import HttpLocust, TaskSet
from Testlist import testlist
from servers_enum import *
import os
from configparser import ConfigParser



#从配置文件取数据
cp = ConfigParser()
cp.read("conf.ini")
section = cp.sections()[2]
ServerName = cp.get(section, "ServerName")
serverhosts = cp.get(section, 'serverhosts')
testNum = cp.get(section,'testNum')

for serverport in servers:
    if os.getenv("ServerName",ServerName) == str(serverport.name):
        port = str(serverport.value)
        hostserver = "http://" + os.getenv("serverhosts",serverhosts) + ":" + port




class UserTask(TaskSet):
    num = int(os.getenv("testNum",testNum))
    tests = testlist(port)
    tasks=[tests[num]]


class User(HttpLocust):
    task_set = UserTask
    host = hostserver
    min_wait = 5000
    max_wait = 8000







