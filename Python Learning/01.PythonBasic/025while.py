# 025while.py
n = int(input("请输入1000000以内的整数"))
i = 1
s = 0
while i <= n:
	t = 1/(2*i-1)
	if i % 2 == 0:
		s -= t
	else:
		s += t
	i += 1
print("1/1-1/3+1/5-1/7+1/9……+1/(2*n-1)的和为", s)
print("乘四等于", s * 4)

# way 2
n = 1
sign = 1
s = 0
while n <= 1000000:
	s += sign * 1 / (2 * n - 1)
	sign = sign * - 1
	n += 1
print(s)