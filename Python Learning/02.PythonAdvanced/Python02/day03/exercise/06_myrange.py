# 练习:
#   写一个myrange函数，此函数返回一个符合range规则的整数列表
#   如:
#     L = myrange(3)
#     print(L)  # [0,1,2]
#     L = myrange(3, 6)
#     print(L)  # [3, 4, 5]
#     L = myrange(1, 10, 3)
#     print(L)  # [1, 4, 7]


def myrange(start, stop=None, step=1):
    # 如果传入一个参数,start绑定0,stop绑定第一个参数
    if stop is None:
        stop = start
        start = 0
    L = []
    i = start  # 用i绑定一个开始值
    while i < stop:
        # 把i放到L列表中
        L.append(i)
        # 按step来递增i
        i += step
    return L

L = myrange(3)
print(L)  # [0,1,2]
L = myrange(3, 6)
print(L)  # [3, 4, 5]
L = myrange(1, 10, 3)
print(L)  # [1, 4, 7]
