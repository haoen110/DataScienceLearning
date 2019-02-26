#while03.py
s = int(input("输入一个数做一个正方形"))
i = 1
while i <= s:
	j = 1
	while j <= s:
		print(j, end=' ')
		j += 1
	print()
	i += 1