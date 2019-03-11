# 028math.py
import math
n = int(input("请输入n"))
sn = sum(list((map(lambda i: i/math.factorial(i), range(1, n+1))))) + 1
print(sn)