# 011.py
def isprime(x):
	if x <= 1:
		return False
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

print(isprime(3))

def prime_m2n(m, n):
	L = []
	for i in range(m, n):
		if isprime(i):
			L.append(i)
	return L

print(prime_m2n(1, 10))

def prime(n):
	L = []
	for i in range(n):
		if isprime(i):
			L.append(i)
	return L

print(prime(20))
print(sum(prime(20)))