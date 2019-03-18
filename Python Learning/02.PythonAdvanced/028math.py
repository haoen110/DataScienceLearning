# 028math.py
import math

def fun(n):
	return sum((map(lambda i: i/math.factorial(i), range(1, n+1))))
	
n = int(input("请输入n："))

print(fun(n))