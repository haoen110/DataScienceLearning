# student_info.py
'''
操作模块

这个模块包含有添加、删除、修改
'''
from Student import Student


def input_student():
	Li = []
	while True:
		name = input("请输入学生姓名：")
		if not name:
			break
		age = input("请输入学生年龄：")
		score = input("请输入学生成绩：")
		# d = {'name':name, 'age':age, 'score':score}
		d = Student(name, age, score)
		Li.append(d)
	return Li

def output_student(Lo):
	Lname = []
	for i in Lo:
		Lname.append(len(i.get_infos()[0]))
	m1 = max(Lname) # 来判断最长的姓名长度
	line1 = ('+' + '-' * (m1+2) + '+' + '-' * (6) + '+' + '-' * (7) + '+') 
	line2 = ('|' + 'name'.center(m1+2) + '|' + 'age'.center(6) + '|'+ 'score'.center(7) + '|')
	print(line1)
	print(line2)
	print(line1)
	for d in Lo:
		n, a, s = d.get_infos()
		t = (n.center(m1+2),
			 str(a).center(6),
			 str(s).center(7))
		line3 = "|%s|%s|%s|" % t
		print(line3)
	print(line1)

def alter_student(La):
	s = input("请输入要修改的学生名字:")
	age = int(input("请输入%s的年龄:" % s))
	score = int(input("请输入%s的分数:" % s))
	for i in La:
		# if i['name'] == s:
		if i.is_name(s):
			i.set_age(age)
			i.set_score(score)
		else:
			print("您输入的姓名不存在！")
	return La

def delete_student(Ld):
	s = input("请输入要删除学生的名字")
	for i in range(len(Ld)):
		if Ld[i].is_name(name):	
			del Ld[i]
			break
		else:
			print("您输入的姓名不存在！")
	return Ld

def sort_age(d):
	return d.get_infos[1]

def sort_score(d):
	return d.get_infos[2]

def save_to_file(L, filename='si.txt'):
	try:
		f = open(filename, mode='x')
	except FileExistsError:
		f = open(filename, mode='a')
	for stu in L:
		stu.write_to_file(f)
		print("保存成功")
	f.close()

def read_from_file(filename='si.txt'):
	L = []
	try:
		f = open(filename)
		for i in f:
			s = i.rstrip() # 去掉换行符
			lst = s.splite(',') # ['xx','xx',xx]\
			name, age, score = lst
			age = int(age)
			score = int(score)
			L.append(Student(name, age, score))
		f.close()
	except:
		print("加载失败")	
	return L

print("student_info被调用")




