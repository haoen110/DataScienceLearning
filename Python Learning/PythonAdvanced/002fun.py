# 002fun.py
def myfun(a, b):
	print("最大值是", max(a, b))
	print("最小值是", min(a, b))
	print("两数和是", a + b)
	print("两数积是", a + b)
	L = [x for x in range(a, b) if x % 2 == 0]
	print("中间的偶数有", L)
myfun(3, 10)
