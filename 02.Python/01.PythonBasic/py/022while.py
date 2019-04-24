# 022while.py
n = int(input("请输入一个数，打印指定宽度的正方形"))
i = 1
while i <= n:
	j = 1
	while j <= n:
		print(j, end=' ')
		j += 1
	print()
	i += 1

