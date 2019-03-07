# 015.py
mysum = lambda n: sum(list(range(1,n+1)))
print(mysum(100))

# myfac = lambda n: s for i in range(1,n+1) s *= i
# print(myfac(5))

def myfac(n):
	a = 1
	for i in range(1, n+1):
		a *= i
	return a
print(myfac(5))

mysum2 = lambda n: sum(list(range(1, n+1)))



