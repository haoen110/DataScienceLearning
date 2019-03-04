# 039dict.py
s = input("请输入一串字符串")
d = {}
for i in s:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1
print(d)

s = input("请输入一串字符串")
d = {}
for i in s:
	d[i] = 0
for i in d:
	d[i] = s.count(i)
for k in d:
	print(k,':',d[k], '次')

