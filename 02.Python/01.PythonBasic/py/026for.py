# 026for.py
n = input("任意输入一个字符串，判断有几个空格")
s = 0
for i in n:
	if i == ' ':
		s += 1
print(s,"个")