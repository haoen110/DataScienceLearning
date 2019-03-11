# 004fun.py
def factor(a):
	L = []

	for i in range(1, a//2 + 1):
		if a % i == 0:
			L.append(i)

	return(L)

i = 1
L = []
while True:
	if sum(factor(i)) == i:
		L.append(i)
	i += 1
	if len(L) == 4:
		break

print(L)