# 045set.py
s = {'hao1', 'hao2', 'hao3', 'hao4', 'hao5'}
s2 = set()
for i in s:
	print(i)
	a = input("若到达，请输入y：")
	if a == 'y':
		continue
	else:
		s2.add(i)
print("以下同学没到：",s2)