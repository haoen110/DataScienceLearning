
# -*- coding:utf-8 -*-

# 01_myhello.py

import sys

if sys.version[0] == '2':
    print("我运行在python2里")
elif sys.version[0] == '3':
    print("我运行在python3里")

if sys.version_info[0] == 2:
    print("python2")
elif sys.version_info[0] == 3:
    print('python3')

print("当前的主版本号是:", sys.version_info.major,
      "当前的次版本号是:", sys.version_info.minor,
      "当前的微版本号是:", sys.version_info.micro)
