# 07_sys_stdin.py



import sys

s = sys.stdin.readline()
print('从键盘读取的第一行是', s)

s = sys.stdin.read()
print('read读取的信息是:', s)

print("程序退出")