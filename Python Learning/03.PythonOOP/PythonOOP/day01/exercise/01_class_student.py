# 练习:
#   定义一个学生类:
#      class Student:
#         def set_info(self, name, age):
#             '''此方法用来给学生对象添加'姓名'和'年龄'属性
#             # 此处自己实现
#         def show_info(self):
#             '''此处显示此学生的信息'''
#     如:
#       s1 = Student()
#       s1.set_info('小张', 20)
#       s2 = Student()
#       s2.set_info('小李', 18)
#       s1.show_info()  # 小张 今年 20 岁
#       s2.show_info()  # 小李 今年 18 岁



class Student:
    def set_info(self, name, age=0):
        '''此方法用来给学生对象添加'姓名'和'年龄'属性'''
        self.name = name
        self.age = age

    def show_info(self):
        '''此处显示此学生的信息'''
        print(self.name, '今年', self.age, '岁')


s1 = Student()
s1.set_info('小张', 20)
s2 = Student()
s2.set_info('小李', 18)
s1.show_info()  # 小张 今年 20 岁
s2.show_info()  # 小李 今年 18 岁

