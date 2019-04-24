# 021recursion.py
def myfac(x):
	if x == 1:
		return 1
	return x * myfac(x - 1)
print(myfac(5))