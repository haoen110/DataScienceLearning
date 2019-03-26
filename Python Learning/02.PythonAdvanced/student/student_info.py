# student_info.py
'''
操作模块

这个模块包含有添加、删除、修改
'''
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
	for d in Lo:
		t = (d['name'].center(m1+2),
			 str(d['age']).center(6),
			 str(d['score'].center(7)))
		line3 = "|%s|%s|%s|" % t
		print(line3)
	print(line1)

def alter_student(La):
	s = input("请输入要修改的学生名字:")
	age = input("请输入%s的年龄:" % s)
	score = input("请输入%s的分数:" % s)
	for i in La:
		if i['name'] == s:
			i['age'] = age
			i['score'] = score
		else:
			print("您输入的姓名不存在！")
	return La

def delete_student(Ld):
	s = input("请输入要删除学生的名字")
	for i in range(len(Ld)):
		if Ld[i]['name'] == s:	
			del Ld[i]
			break
		else:
			print("您输入的姓名不存在！")
	return Ld

def sort_age(d):
	return d['age']

def sort_score(d):
	return d['score']

def save(L):
	try:
		f = open('./si.txt', mode='x')
	except FileExistsError:
		f = open('./si.txt', mode='a')
	for i in L:
		L1 = [j for j in i.values()]
		s = ','.join(L1)+'\n'
		f.writelines(s)
	f.close()

def load():
	try:
		f = open('./si.txt')
	except:
		print("加载失败")	
	for i in L:
		L1 = [j for j in i.values()]
		s = ','.join(L1)+'\n'
		f.writelines(s)
	f.close()


print("student_info被调用")




