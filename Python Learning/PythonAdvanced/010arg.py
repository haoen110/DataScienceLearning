# 010arg.py
def myrange(start, stop=None, step = 1):
	if stop is None:
		stop = start
		start = 0
	L = []
	i = start
	while i < stop:
		L.append(i)
		i += step
	return L

L = myrange(3)
print(L) # [0, 1, 2]
L = myrange(3, 6)
print(L) # [3, 4, 5]
L = myrange(1, 10, 3)
print(L) # [1, 4, 7]