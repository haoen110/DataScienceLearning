# 007arg.py
def sum3(a, b, c):
	return a + b + c

def pow3(x):
	return x ** 3

print("1**3 + 2**3 + 3**3 =", pow3(1) + pow3(2) + pow3(3))
print("(1 + 2 + 3)**3 =", pow3(sum3(1, 2, 3)) )