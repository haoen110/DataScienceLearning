
# 此示例示意位置传参 

# 以后所有函数都用myfun不变来示意参数传递
def myfun(a, b, c):
    print('a绑定的是:', a)
    print('b绑定的是:', b)
    print('c绑定的是:', c)


# 此处用关键字传参方式给myfun传参
myfun(b=22, c=33, a=11)  # 等同于myfun(11,22,33)
myfun(c=3, b=2, a=1)