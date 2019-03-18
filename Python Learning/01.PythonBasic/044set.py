# 044set.py
L = []
while True:
	s = input("请输入单词，为空时结束")
	if not s:
		break
	L.append(s)

s = set(L)
print("有%d个单词" % len(s))

for x in L:
	if x in s:
		print(x)
		s.discard(x)




