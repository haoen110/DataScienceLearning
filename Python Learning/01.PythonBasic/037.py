# 037.py
s = 'ABC'
s1 = '123'
L = [x + y for x in s for y in s1]
print(L)

# 方法1
L = [1, 3, 2, 1, 6, 2, 4, 4, 8]
L1 = []
for i in range(len(L)):
	if L[i] in L1:
		continue
	L1.append(L[i])
print(L1)

# 斐波那契方法
n = 40
L = [1, 1]
while len(L) < 40:
	L.append(L[-2] + L[-1])
print(L)
# 斐波那契方法
a = 0
b = 1
L = []
while len(L) < 40:
	a, b = b, a + b
	L.append(a)
print(L)

a = 1
for i in range(5):
	if i == 2:
		break
		a += 1
	else:
		a += 1
print(a)