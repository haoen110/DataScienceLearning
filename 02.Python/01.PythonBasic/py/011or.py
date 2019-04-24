# 011or.py
s = int(input("请输入成绩：") or '0')
if s < 0 or s > 100:
	print("您的成绩不合法")
else:
	print("您输入的成绩是", s)