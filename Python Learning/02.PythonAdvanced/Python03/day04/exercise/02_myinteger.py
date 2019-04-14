# 练习：
# 　　写一个生成器函数:
#     def myinteger(n):
#         ....
#     此生成器函数可以生成从0开始，的一系列的整数,到n结束(不包含n)

#     for x in myinteger(3):
#         print(x)   # 打印 0, 1, 2
#     it = iter(myinteger(2))
#     print(next(it))  # 0
#     print(next(it))  # 1
#     print(next(it))  # StopIteration异常


def myinteger(n):
    # 方法1
    # i = 0
    # while i < n:
    #     yield i  # 把i送回给next函数
    #     i += 1
    # 方法2
    for y in range(n):
        yield y


for x in myinteger(3):
    print(x)   # 打印 0, 1, 2

it = iter(myinteger(2))
print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # StopIteration异常
