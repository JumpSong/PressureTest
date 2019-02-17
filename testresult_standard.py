# -*- coding: utf-8 -*-
from servers_enum import *
#1：压侧结果标准值


def result_standard(server,num):
    if server==servers.User.name:
        user =[[200,100],[200,150],[200,100]]
        return user[num]
    if server==servers.Param.name:
        param = [[200,100],[200,150],[200,100]]
        return param[num]
