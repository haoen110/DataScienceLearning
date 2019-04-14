import os,sys 

#结束进程后不在执行后面内容
# os._exit(0)

try:
    sys.exit("hello world")
except SystemExit as e:
    print("退出:",e)

print("process exit")