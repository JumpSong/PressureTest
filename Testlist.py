# -*- coding: utf-8 -*-
import sys
import os
ROOT_PATH =  os.path.dirname(os.path.abspath("__file__"))
sys.path.append(ROOT_PATH)

from testerDatabase import *




cacheEnable = os.getenv("CacheEnable",'True')

def testlist(port):
    common = Common()
    common.cache(cacheEnable)#缓存
    testlist = list()
    testlist.clear()
    if port == str(servers.Homepage.value):
        homepage = Run_HomePage_Test
    elif port == str(servers.Main.value):
        pass




