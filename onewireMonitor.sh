#!/bin/sh

ps auxw | grep onewireMonitor_py3.py | grep -v grep > /dev/null
result=$?
echo "exit code: ${result}"
#if [ $? != 0 ]
if [ ${result} -eq "0" ]; then
        echo "Process Running, doing nothing"
else
        echo "starting onewireMonitor"
        nohup /usr/bin/python3 /usr/local/sbin/onewireMonitor_py3.py > /dev/null 2>&1 &
        #/usr/bin/python3 /usr/local/sbin/onewireMonitor_py3.py & > /dev/null 2>&1
fi
