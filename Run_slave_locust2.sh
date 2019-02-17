#!/bin/bash

host="192.168.0.97"

locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &
locust -f /root/TL.PressureTest/run_locust.py --slave --master-host=${host} --master-port=5557 >/dev/null 2>&1 &