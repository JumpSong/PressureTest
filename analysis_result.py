# -*- coding: utf-8 -*-
import os,csv,sys
from testresult_standard import *

def get_result():
    if os.path.exists('result_requests.csv'):
        with open("result_requests.csv") as cf:
            reader = csv.reader(cf)
            l = list()
            l1 = list()
            for line in reader:
                lines = reader.line_num
                if lines == 1:
                    continue
                if line[0] == 'None':
                    continue
                l.append(line)
            for i in l:
                s = i[5:][::4]  # 切片,取平均响应时间和RPS的值
                l1.append(s)

        return l1[0]






if __name__=="__main__":
    servername = os.getenv("ServerName", "User")
    testNum = int(os.getenv("testNum", '0'))
    result = get_result()
    result_standard = result_standard(servername, testNum)
    if float(result[0]) > (float(result_standard[0]) + float(100)):
        print("-----------平均响应时间不符合标准(误差+-100)--------------")
        print("平均响应时间实际值：", result[0])
        print("平均响应时间标准值：", result_standard[0])
        print("吞吐量实际值：", result[1])
        print("吞吐量标准值：", result_standard[1])
        sys.exit(0)

    elif float(result[1]) < (float(result_standard[1] - float(50))):
        print("-----------吞吐量不符合标准(误差+—50)--------------")
        print("平均响应时间实际值：", result[0])
        print("平均响应时间标准值：", result_standard[0])
        print("吞吐量实际值：", result[1])
        print("吞吐量标准值：", result_standard[1])
        sys.exit(0)

    elif float(result[1]) > (float(result_standard[1] + float(50))):
        print("-----------平均响应时间稳定,吞吐量性能提升-----------")
        print("平均响应时间实际值：", result[0])
        print("平均响应时间标准值：", result_standard[0])
        print("吞吐量实际值：", result[1])
        print("吞吐量标准值：", result_standard[1])
