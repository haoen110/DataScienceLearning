# return.py

# 问题 ：
#   函数如何能返回一些数据给调用者?
#   答案就是: return 语句 
s = 1
def myfun(a, b):
    s = a + b
    print("和是: ", s)
    return 10000

v = myfun(100, 200)
print('v =', v)  # 10000
print(s)  # 可以吗？

