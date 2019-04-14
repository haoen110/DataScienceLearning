# 02_recursion_deep.py


# 此示例示意递归层数的控制
def fx(n):
    print("递归进入第", n, "层")
    if n == 3:
        return
    fx(n + 1)
    print("递归退出第", n, '层')

fx(1)
print("程序结束")
