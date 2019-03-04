# 042students.py
L = []
while True:
	n = input("请输入学生姓名：")
	if n:
		a = input("请输入学生年龄：")
		s = input("请输入学生成绩：")
		d = {'name':n, 'age':a, 'score':s}
		L.append(d)
	else:
		break

Ln = list(i['name'] for i in L) # 将列表中的字典中的姓名提取出来
m1 = len(max(Ln)) # 来判断最长的姓名长度

line1 = ('+' + '-' * (m1+2) + '+' + '-' * 5 + '+' + '-' * 7 + '+') 
line2 = ('|' + 'name'.center(m1+2) + '|' + 'age'.center(5) + '|'+ 'score'.center(7) + '|')
print(line1)
print(line2)
print(line1)

for i in L:
	print('|' + i['name'].center(m1+2) + '|' + str(i['age']).center(5) + '|' + str(i['score']).center(7) + '|' )
print(line1)