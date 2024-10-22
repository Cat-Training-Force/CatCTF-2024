#!/bin/sh
nohup python app.py > /tmp/app.log 2>&1 & sleep 5
# Web 服务启动后执行下一个命令
echo "Web 服务已启动，执行下一个命令"
unset GZCTF_FLAG
tail -f /tmp/app.log
