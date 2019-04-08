# 3. 写一个函数，求
#     1 + 2**2 + 3**3 + ... + n**n的和
#     (n给个小点的数)


def power_sum(n):
    # 方法1
    # s = 0
    # for x in range(1, n + 1):
    #     s += x**x
    # return s

    # 方法2
    return sum(map(lambda x: x**x,
                   range(1, n + 1)))


print("power_sum(10) =", power_sum(10))
