# 029random.py
import random as rd
x = rd.randrange(101)
s = 0
while True:
	s += 1
	y = int(input("请输入您猜的数："))
	if y < x:
		print("您猜小了")
	elif y > x:
		print("您猜大了")
	elif y == x:
		print("您猜对了！")
		break
print("您猜了%d次" % s)
