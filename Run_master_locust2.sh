#!/bin/bash
export PATH=$PATH:/home/ssm/.local/bin/


locust --master --master-bind-port=5557 --master-bind-host=192.168.0.97 -f run_locust.py