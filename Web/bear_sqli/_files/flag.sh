#!/bin/bash

# 确保 GZCTF_FLAG 变量已经定义
if [ -z "$GZCTF_FLAG" ]; then
  export GZCTF_FLAG="catctf{this_is_test_flag_for_sql_union_injection}"
  exit 1
fi

# 使用更安全的方式来引用用户名
mysql -e "USE ctftraining; UPDATE users SET flag = '$GZCTF_FLAG' WHERE username = 'guest';" -uroot -proot

# 安全地删除文件
if [ -f /flag.sh ]; then
  rm -f /flag.sh
fi