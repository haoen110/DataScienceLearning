# 003fun.py
def fun(a):
	s = 1
	for i in range(a):
		s = 2 * (s + 1) 
	return s
print(fun(9))

s = 1543
for _ in range(9):
	s = s / 2 - 1
print(s)
