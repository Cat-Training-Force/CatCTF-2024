#!/bin/bash
docker run --platform linux/amd64 -itd -p8102:5000 -e GZCTF_FLAG=flag{local_test_flag} --name bear_hacker whistleh/catctf:bear_hacker