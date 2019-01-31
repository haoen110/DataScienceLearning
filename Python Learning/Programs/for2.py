#for2.py
for i in range(20):
	print(i, end=' ')
else:
	print()

for i in range(100):
	if (i * (i + 1)) % 11 == 8:
		print(i)
	else:pass
else:pass

s = 0
for i in range(1,100,2):
	s += i
else:print(s)

i = 1
s = 0
while i <= 99:
	s += i
	i += 2
else:
	print(s)

w = int(input("请输入宽度："))
for _ in range(w):
	for x in range(1, w + 1):
		print(x, end=' ')
	print()

w = int(input("请输入宽度："))
for y in range(1, w + 1):
	for x in range(y, y + w):
		print("%2d"%x, end=' ')
	print()

