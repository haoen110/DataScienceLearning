#break.py
i = 1
while i <= 6:
	print("本次循环开始时：", i)
	if i ==3:
		break
	print("本次循环结束时：", i)
	i += 1

while True:
	n = int(input("请输入数字，当为0时结束"))
	if n == 0:
		break
	print(n)
