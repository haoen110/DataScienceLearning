# 031try.py
def get_score():
	try:
		n = int(input("请输入学生的成绩："))
		if 0 <= n <= 100:
			return n
		return 0
	except:
		print("出现异常，成绩为0分")
		return 0

score = get_score()
print("该同学的成绩为：", score)