# 032.py
def fall_h(n):	
	h = 100
	for i in range(1, n+1):
		h = h / 2
	print("高度是：", h, "米")
	return h

def fall_d(n):
	d = 100
	h = 0
	for i in range(1, n+1):
		h = d + d/2
		d = d/2
	print("高度是", h, "米")
	print("路程是", d, "米")

def is_prime(x):
	if x <= 1:
		return False
	for i in range(2, x):
		if x% i == 0:
			return False
	return True

def get_prime_list(n):
	'''次函数根据给定的一个整数，返回所有因数的列表'''
	L = [] #用来存放因数
	# 如果n不是素数，我们就拆出因数出来
	while not is_prime(n):
		# 把n拆出来一个素数因数，人后循环
		# 找n的一个因数
		for x in range(2, n):
			if is_prime(x) and n % s == 0:
				L.append(x)
				n /= x 
				n = int(n)
				break
	else:
		L.append(n)
	return L

n = int(input("请输入整数："))
print(get_prime_list(n))


