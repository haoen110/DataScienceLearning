# 021while.py
s = 0
i = 1
while i <= 100:
	s += i
	i += 1
else:
	print("1～100的和为：%d" % s)

n = int(input("请输入三角形的高度"))
i = 1
while i <= n:
	print(i * "*")
	i += 1

j = 1
while j <= 10:
	i = 1 
	while i <= 20:
		print(i, end=' ')
		i += 1
	print("End!")
	j += 1
