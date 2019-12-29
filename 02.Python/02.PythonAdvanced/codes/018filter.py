# 018filter.py
even = [x for x in filter(lambda x: x % 2 == 0, range(20))]
print(even)

def isprime(x):
	if x < 2:
		return False
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

prime = [x for x in filter(isprime, range(1, 20))]
prime = list(filter(isprime, range(1, 20)))
print(prime)