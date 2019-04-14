# 04_sys_exit.py


def f():
    print("f开始调用")
    import sys
    sys.exit(0)
    print('f()结束调用')

f()
print("程序结束")