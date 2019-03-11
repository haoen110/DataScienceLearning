# 022.py
def myfac(n):
	if n == 1:
		return 1
	return n * myfac(n - 1)

sum = sum(map(myfac, range(1, 21)))
print(sum)

L = [[3,5,8], 10, [[13,14], 15, 18], 20]
def print_list(lst):
	for i in lst:
		if type(i) is list:
			print_list(i)
		else:
			print(i)
print_list(L)
