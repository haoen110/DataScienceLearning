# 015.py
mysum1 = lambda n: sum(list(range(1,n+1)))
def mysum2(n):
	return sum(range(1, n+1))
def mysum3(n):
	if n == 1:
		return 1
	return n + mysum3(n - 1)

print(mysum1(100), mysum2(100), mysum3(100))

# myfac = lambda n: s for i in range(1,n+1) s *= i
# print(myfac(5))

def myfac1(n):
	a = 1
	for i in range(1, n+1):
		a *= i
	return a

def myfac2(x):
	if x == 1:
		return 1
	return x * myfac2(x - 1)
print(myfac1(5), myfac2(5))	

def power_sum1(n):
	s = 0
	for x in range(1, n + 1):
		s += x ** x
	return s
def power_sum2(n):
	return sum(map(lambda x: x**x, range(1, n + 1)))
print(power_sum2(5), power_sum1(5))



