# 032prime.py
n = int(input("请输入一个整数，判断是否为素数"))
for i in range(2, n):
	if n % i == 0:
		print("不是素数")
		break
else:
	print("是素数")


n = int(input("请输入一个整数，判断是否为素数"))
flag = True

for i in range(2, n):
	if n % i == 0:
		flag = False
		break

if flag == True:
	print(n, "是素数")
else:
	print(n, "不是素数")