# 033gen.py
def myinterger(n):
	s = 0
	while s < n:
		yield s
		s += 1

for x in myinterger(3):
	print(x)

it = iter(myinterger(3))
print(next(it))
print(next(it))
print(next(it))
print(next(it))