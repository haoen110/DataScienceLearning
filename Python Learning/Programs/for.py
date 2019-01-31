#for.py 字符串迭代
s = 'ABCDE'
for ch in s:
	print('ch -> ', ch)
else:
	print("执行else")
print("End")

#计算空格的个数
a = input("输入字符串")
b = 0
for i in a:
	if i == ' ':
		b += 1
print(b)

for x in range(4):
	print(x)

#for2.py
for i in range(20):
	print(i, end = ' ')
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










