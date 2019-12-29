# 010abs.py
n = int(input("请输入一个数，求他的绝对值"))
if n < 0:
	print(-n)
else:
	print(n)

n = int(input("请输入一个数，求他的绝对值"))
print(n) if n > 0 else print(-n)