# 017str.py
s = input("请输入字符串，判断有几个空格")
print(s.count(" "))

s = input("请输入字符串，去处前后的空白字符")
print(s.strip())

s = input("请输入字符串，判断是否为数字")
if s.isdigit():
	print("是数字")
else:
	print("不是数字")