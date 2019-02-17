# -*- coding: utf-8 -*-

# ROOT_PATH =  os.path.dirname(os.path.abspath("__file__"))
# sys.path.append(ROOT_PATH)
import csv,requests
from MicroService.UserServer_Tests import *
from testresult_standard import *


# class resutls():
#     def test(self):
#         with open("result_requests.csv") as cf:
#             reader = csv.reader(cf)
#             l = list()
#             l1 = list()
#             for line in reader:
#                 lines = reader.line_num
#                 if lines == 1:
#                     continue
#                 if line[0] =='None':
#                     continue
#                 l.append(line)
#             for i in l:
#                 s = i[5:][::4]#切片,取平均响应时间和RPS的值
#                 l1.append(s)
#         print(l1[0][1])
#         return l1[0]
#
#     # for j in range(1, 100):
#     #     ids = list()
#     #     ids.clear()
#     #     for k in range(1, 21):
#     #         ids.append((random.randint(1, 1000)))
#     #     print(ids)
#     # tests = testlist(port)
#     #
#     # print(tests)
#
#
#
# def get_funtion(fun):
#     testlist = list()
#     for i in fun.keys():
#         if i[0:4]!='test':
#             continue
#         testlist.append('user.'+i)
#     print(testlist)
#     return testlist
#
#
# def get_funtion2(fun):
#     testlist = list()
#     for i in fun.values():
#         if type(i).__name__=='function':
#             print(i)
#             testlist.append(i.__dict__)
#     fun.values()
#     print(testlist[1])
#     return testlist
#
#
# def test():
#     s = "222-----------平均响应时间不符合标准-----------111"
#     if '3' in s or '平均响应时间' in s:
#         print(s)
#     return



if __name__== "__main__":
    # basehost = '192.168.1.157'
    # hosts = basehost.split('192.168.1.')[1]
    # print(hosts)
    l = {}
    l ['name'] = 1
    print(l)
