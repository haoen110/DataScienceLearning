# 024while.py
n = int(input("请输入三角形的高度"))
i = 1
while i <= n:
	print(' ' * (n - i) + '*' * i)
	i += 1

i = 1
while i <= n:
	print(' ' * (i - 1) + '*' * (n - i + 1))
	i += 1

i = 1
while i <= n:
	print('*' * (n - i + 1) + ' ' * (i - 1))
	i += 1