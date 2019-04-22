
# 此示例示意位置传参 

# 以后所有函数都用myfun不变来示意参数传递
def myfun(a, b, c):
    print('a绑定的是:', a)
    print('b绑定的是:', b)
    print('c绑定的是:', c)


# 此处用拆解字典的方式给myfun传参
d = {'c': 33, 'b': 22, 'a': 11}
myfun(**d)  # 拆解字典后再传参

# 以下是错误的用法
# d1 = {'c': 33, 'b': 22, 'a': 11, 'd': 44}
# myfun(**d1)  # 拆解字典后再传参