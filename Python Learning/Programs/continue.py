#continue.py
n = int(input("请输入一个数"))
for i in range(n):
	if i % 2 == 0:
		print(i)
	else:
		continue

s = 0
for i in range(1,101):
	if i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
		s += i
print(s)