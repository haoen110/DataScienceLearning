# 016students.py
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

def alter_student(La):
	s = input("请输入要修改的学生名字:")
	age = input("请输入%s的年龄:" % s)
	score = input("请输入%s的分数:" % s)
	for i in La:
		if i['name'] == s:
			i['age'] = age
			i['score'] = score
	return La

def delete_student(Ld):
	s = input("请输入要删除学生的名字")
	for i in range(len(Ld)):
		if Ld[i]['name'] == s:	
			del Ld[i]
			break
	return Ld

def main():
	print("+-------------------+")
	print("| 1)添加学生生信息  |")
	print("| 2)查看所有学生信息|")
	print("| 3)修改学生信息    |")
	print("| 4)删除学生信息    |")
	print("| q)退出            |")
	print("+-------------------+")

	global L 

	s = input("请选择：")
	if s == '1':
		L += input_student()
	elif s == '2':
		output_student(L)
	elif s =='3':
		output_student(L)
		alter_student(L)
		print("修改后的数据为：")
		output_student(L)
	elif s =='4':
		output_student(L)
		delete_student(L)
		print("删除后的数据为：")
		output_student(L)
	elif s =='q':
		exit()

L = []
while True:
	main()

# L = input_student()
# output_student(L)	
# print("再添加几个学生信息")
# L += input_student()
# print("添加学生后的学生信息如下：")
# output_student(L)
