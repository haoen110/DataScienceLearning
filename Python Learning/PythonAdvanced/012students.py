# 012students.py
def input_student():
	Li = []
	while True:
		name = input("请输入学生姓名：")
		if not name:
			break
		age = input("请输入学生年龄：")
		score = input("请输入学生成绩：")
		d = {'name':name, 'age':age, 'score':score}
		Li.append(d)
	return Li

def output_student(Lo):
	Lname = []
	for i in Lo:
		Lname.append(len(i['name']))
	m1 = max(Lname) # 来判断最长的姓名长度
	line1 = ('+' + '-' * (m1+2) + '+' + '-' * (6) + '+' + '-' * (7) + '+') 
	line2 = ('|' + 'name'.center(m1+2) + '|' + 'age'.center(6) + '|'+ 'score'.center(7) + '|')
	print(line1)
	print(line2)
	print(line1)
	for d in L:
		t = (d['name'].center(m1+2),
			 str(d['age']).center(6),
			 str(d['score'].center(7)))
		line3 = "|%s|%s|%s|" % t
		print(line3)
	print(line1)

L = input_student()
output_student(L)	
print("再添加几个学生信息")
L += input_student()
print("添加学生后的学生信息如下：")
output_student(L)
