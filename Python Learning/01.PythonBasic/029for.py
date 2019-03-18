# 029for.py
n = int(input("请输入数字代表正方形的宽度"))
for i in range(1, n+1):
	for j in range(i , n + i):
		print("%2d" % j, end=' ')
	print()

