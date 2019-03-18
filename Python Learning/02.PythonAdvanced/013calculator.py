# 013calculator.py
def myadd(x, y):
	return x+y
def mymul(x, y):
	return x*y





def get_op(s): # s代表操作字符串
	if s == "加" or s == '+':
		return myadd
	elif s == "乘" or s == '*':
		return mymul

def main():
	while True:
		s = input("请输入计算公式：") # 如：10 加 20
		L = s.split()
		a, s, b = L
		a, b = int(a), int(b)
		fn = get_op(s)
		print("结果是：", fn(a, b)) # 结果是30

main()