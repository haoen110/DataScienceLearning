# 035diedai.py
L = []
while True:
	s = input("请输入：")
	if not s:
		break
	L.append(s)
for i in enumerate(L, 1):
	index, value = i
	print("第%d行：%s" % (index,value))
