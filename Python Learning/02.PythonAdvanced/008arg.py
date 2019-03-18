# 008arg.py
def mysum(a, b, c = None):
	if not c:
		return a + b
	return (a + b) % c

print(mysum(1,100))
print(mysum(2, 10, 7))