# 035list.py
L = []
while True:
	s = input("请输入字符，为空时结束")
	if not s:
		break
	L.append(s)
L.reverse()
i = 0
s = 0
while i < len(L):
	print(L[i])
	s += len(L[i])
	i += 1
print(s)

