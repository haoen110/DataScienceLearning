# 练习:
#   1. 将 1 ~20 内的偶数用filter筛选出来，形成列表
#   2. 用filter函数将1~100之间的所有素数(prime) 放入
#      到列表中


#   1. 将 1 ~20 内的偶数用filter筛选出来，形成列表
L = [x for x in filter(lambda x: x % 2 == 0,
                       range(1, 20))]
print(L)
L = list(filter(lambda x: x % 2 == 0, range(1, 20)))
print(L)

#   2. 用filter函数将1~100之间的所有素数(prime) 放入
#      到列表中
def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

L = list(filter(isprime, range(100)))
print(L)
