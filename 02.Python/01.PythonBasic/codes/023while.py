# 023while.py
s = 0
while True:
	n = int(input("请输入一些整数，每次输入一个，当输入负数时结束输入"))
	if n < 0:
		break
	s += n
print("您输入的和为：%d" % s)