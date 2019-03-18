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

def myrange(start=0, stop, step=1):
	if start == 0:
		stop = start
	i = start
	while i < stop:
		yield i
		i += step

for x in myrange(10):
	print(x)

def myrange(start = 0, stop, step = 1):
	print(start, stop, step)

myrange(1,2,3)

