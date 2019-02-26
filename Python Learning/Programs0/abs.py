#abs.py

a = int(input("1、请输入一个数"))
if a < 0 :
	print("该数的绝对值为：", -a)
else:print("该数的绝对值为：", a)



a = int(input("2、请输入一个数"))
b = -a if a < 0 else a
print("该数的绝对值为：", b)

