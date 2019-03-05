# 011.py
def isprime(x):
	for i in range(2, x):
		if x % i == 0:
			return False
		return True

print(isprime(3))

def prime_m2n(m, n):
	L = []
	if m <= 2:
		L.append(2)
	for i in range(m, n):
		if isprime(i):
			L.append(i)
	return L

print(prime_m2n(1, 10))

def prime(n):
	L = []
	if n > 2:
		L.append(2)
	for i in range(n):
		if isprime(i):
			L.append(i)
	return L

print(prime(20))
print(sum(prime(20)))