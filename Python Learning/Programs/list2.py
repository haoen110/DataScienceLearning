#list2.py
L = []
while True:
	s = input("请输入字符串")
	if s != '':
		L.append([s])
	else:break
L.reverse()

print(L)
