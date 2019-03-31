# 03_factorial_sum.py

# 3. 请编写函数fun,其功能是计算下列多项式的和
#    sn = 1 + 1/1! + 2/2! + 3/3! + ... n/n!
#    计算n为100时的值
#   看一下求出来的和是什么?
#   (建议用math.factorial)

import math

def fun(n):
    formula = lambda x: 1 / math.factorial(x)
    return sum(map(formula, range(n + 1)))


print('n=100时,fun(100)=', fun(100))