

# 此示例示意位置传参 

# 以后所有函数都用myfun不变来示意参数传递
def myfun(a, b, c):
    print('a绑定的是:', a)
    print('b绑定的是:', b)
    print('c绑定的是:', c)


# 此处用拆解序列方式调用myfun函数
s = [1, 2, 3]
myfun(*s)  # * 表示把s拆开  等同于myfun(s[0], s[1], s[2])
s2 = "ABC"
myfun(*s2)
