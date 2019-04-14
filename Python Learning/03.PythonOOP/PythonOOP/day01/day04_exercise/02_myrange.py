# 2. 仿制range函数的功能，写一个生成器函数myrange,
#  要求功能与range功能相近，能实现一个，两个，三个参数
#  传参,生成正向的整数
#   如:
#     for x in myrange(1, 10, 3):
#        print(x)   # 1, 4, 7

def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    i = start
    while i < stop:
        yield i
        i += step  # 增加i的值,供下次生成



print(list(myrange(5)))  # [0, 1, 2, 3, 4]

print(list(myrange(10, 15)))  #  [10, 11, 12, ...]

for x in myrange(1, 10, 3):
   print(x)   # 1, 4, 7