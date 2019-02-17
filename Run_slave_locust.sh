#!/bin/bash
export client=${1}
export request=${2}
export runtime=${3}
export CacheEnable=${4}
export  ServerName=${5}
export serverhosts=${6}
export Httptype=${7}
export testNum=${8}
host="192.168.0.97"

locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &


