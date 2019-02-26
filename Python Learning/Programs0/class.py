#class.py

#定义一个空的类
class Student():
	pass

#定义一个对象
howie = Student()

#定义一个类，用来描述听Python的学生
class PythonStudent():
	# 用None给不确定的值赋值
	name = None
	age = 100
	course = "Python"

	# def 缩进层级
	# 系统默认self参数
	def doHomeword(self):
		print("I'm working")
		return None

#示例一个叫yueyue的学生
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomeword()