# 009if.py
s = int(input("请输入学生的成绩"))
if 0 <= s <= 100:
	print("您输入的成绩合法")
	if 90 <= s <= 100:
		print("优")
	elif 80 <= s <= 89:
		print("良")
	elif 60 <= s <= 79:
		print("及格")
	else:
		print("不及格")
else:
	print("您输入的成绩不合法")