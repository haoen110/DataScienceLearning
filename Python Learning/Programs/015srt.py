# 015srt.py
s = input("请输入一个字符")
if s:
	print(ord(s[0]))
else:
	print("为空")

s = int(input("请输入0～65535之间的任意一个数"))
if s:
	print(chr(s))
else:
	print("为空")