# 006return.py
def input_number():
	L = []
	while True:
		s = int(input("请循环输入整数，输入负数时结束"))
		if s < 0:
			return L
		L.append(s)

L = input_number()
print(L)
print("用户输入的最大数是：", max(L))
print("用户输入的最小数是：", min(L))
print("用户输入的最和数是：", sum(L))