#grades.py

g = int(input("请输入学生的成绩"))
if 0 <= g <= 100:
	print("属于成绩")
	if 90 <= g <= 100:
		print("优秀")
	elif 90 <= g <= 89:
		print("良好")
	elif 60 <= g <= 79:
		print("及格")
	else:print("不及格")
else:print("不处于成绩范围")

