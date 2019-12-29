# main.py
'''
主模块

这个模块是操作的主模块
'''
from .menu import*
from .student_info import*

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
		elif s == '9':
			save(L)
		elif s =='q':
			return