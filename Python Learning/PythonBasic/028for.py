# 028for.py
for i in range(1,101):
	if (i + 1) * i % 11 == 8:
		print(i, end=' ')
print()

i = 1
s = 0
while i <= 99:
	s += i
	i += 2
print(s)

s = 0
for i in range(1, 100, 2):
	s += i
print(s)
