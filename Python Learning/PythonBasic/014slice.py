# 014slice.py
s = input("请输入字符，将去掉第一个和最后一个字符")
print(s[1:len(s)-1])

s = input("请输入一串文字，判断是否为回文")
if s == s[::-1]:
	print("是回文")
else:
	print("不是回文")
	