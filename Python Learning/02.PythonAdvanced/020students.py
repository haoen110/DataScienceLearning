# 020students.py
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

def show_menu():
	print("+------------------------------+")
	print("| 1) 添加学生生信息            |")
	print("| 2) 查看所有学生信息          |")
	print("| 3) 修改学生信息              |")
	print("| 4) 删除学生信息              |")
	print("| 5) 按成绩从高至低打印学生信息|")
	print("| 6) 按成绩从低至高打印学生信息|")
	print("| 7) 按年龄从大至小打印学生信息|")
	print("| 8) 按年龄从小至大打印学生信息|")
	print("| q) 退出                      |")
	print("+------------------------------+")

def main():
	L = []
	while True:
		show_menu()
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
		elif s == '5':
			L2 = sorted(L, key=sort_score, reverse=True)
			print("按成绩从高至低打印学生信息")
			output_student(L2)
		elif s == '6':
			L2 = sorted(L, key=sort_score)
			print("按成绩从低至高打印学生信息")
			output_student(L2)
		elif s == '7':
			L2 = sorted(L, key=sort_age, reverse=True)
			print("按年龄从大至小打印学生信息")
			output_student(L2)
		elif s == '8':
			L2 = sorted(L, key=sort_age)
			print("按年龄从小至大打印学生信息")
			output_student(L2)
		elif s =='q':
			return

main()

# L = input_student()
# output_student(L)	
# print("再添加几个学生信息")
# L += input_student()
# print("添加学生后的学生信息如下：")
# output_student(L)
