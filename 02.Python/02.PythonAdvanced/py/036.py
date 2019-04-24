# 036.py
def isprime(x):
	if x < 2:
		return False
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

def primes(begin, end):
	for i in range(begin, end):
		if isprime(i):
			yield i

L = [x for x in primes(10, 20)]
print(L)

def myrange(start, stop=None, step=1):
	if not stop:
		stop = start
		start = 0
	i = start
	while i < stop:
		yield i
		i += step # 增加i的值，供下次生成

for x in myrange(10):
	print(x)
