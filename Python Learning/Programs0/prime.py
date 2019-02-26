#prime.py
p = int(input("请输入一个整数，判断是否为素数："))
for i in range(2, p):
	if p % i == 0:
		print("这个数不是素数")
		break
else:print("这个数是素数")

print("The End!")

#2
p = int(input("请输入一个整数，判断是否为素数："))
flag = True
for i in range(2, p):
	if p % i == 0:
		#print("这个数不是素数")
		flag = False
		break
if flag == True:
	print("这个数是素数")
else:
	print("这个数不是素数")