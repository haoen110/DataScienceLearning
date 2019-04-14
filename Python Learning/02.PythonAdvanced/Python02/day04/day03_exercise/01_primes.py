# 1. 素数prime函数练习
#   1)  写一个函数isprime(x)  判断x是否为素数，如果
#       是素数，返回True,否则返回False
#   2) 写一个函数prime_m2n(m, n), 返回从m开始到n结
#      束(不包含n)的范围内的素数列表
#     如:
#       L = prime_m2n(1, 10)
#       print(L) # [2,3,5,7]
#   3) 写一个函数primes(n), 返回指定范围内素数(不包含n)
#      全部素数的列表,并打印这些素数
#     如:
#       L = prime(20)
#       print(L)  # [2,3,5,7,11,13,17,19]
#     1) 打印 100以内的全部素数
#     2) 打印 100以内全部素数的和

def isprime(x):
    if x <= 1:
        return False
    # 判断能否被从2, ... x-1的整除
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prime_m2n(m, n):
    # L = []
    # for i in range(m, n):
    #     if isprime(i):
    #         L.append(i)
    # return L
    # 用列表推导式可以实现
    return [x for x in range(m, n) if isprime(x)]

L = prime_m2n(1, 10)
print(L)  # [2,3,5,7]


def primes(n):
    return prime_m2n(0, n)

L = primes(20)
print(L)  # [2,3,5,7,11,13,17,19]
# 1) 打印 100以内的全部素数
for x in primes(100):
    print(x)
# 2) 打印 100以内全部素数的和
print("100内全部素数的和是:", sum(primes(100)))
