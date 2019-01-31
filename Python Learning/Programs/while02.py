#while_interger.py
i = 1
while i <= 20:
	print(i,end=' ')
	if i % 5 == 0:
		print('\n')
	i += 1
print('The End!')

i = 10
while i >= 1:
	print(i, end=' ')
	i -= 1
else:
	print()

i = 1
s = 0
while i <= 100:
	s += i
	i += 1
else:
	print(s)

h = int(input("请输入三角形高度："))
i = 1
while i <= h:
	print('*'*i,'\n')
	i += 1

j = 1
while j <= 4:
	i = 1
	while i <= 20:
		print(i,end=' ')
		i += 1
	print()
	j += 1
else:print('The End!')