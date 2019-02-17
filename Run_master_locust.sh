#!/bin/bash
set -e
client=${1}
request=${2}
runtime=${3}
export PATH=$PATH:/home/ssm/.local/bin/
export CacheEnable=${4}
export ServerName=${5}
export serverhosts=${6}
export Httptype=${7}
export testNum=${8}


locust --master --master-bind-port=5557 --master-bind-host=192.168.0.97 -f run_locust.py --no-web -c ${client:-"100"} -r ${request:-"10"} -t ${runtime:-"30"} --only-summary --csv-base-name=result


python analysis_result.py
