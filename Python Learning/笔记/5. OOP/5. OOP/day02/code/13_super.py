# 13_super.py

# 此示例示意子类对象用super方法显式调用基类的__init__方法

class Human:
    def __init__(self, n, a):
        '''此方法为人的对象添加，姓名和年龄属性'''
        self.name = n
        self.age = a
    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self, n, a, s=0):
        super().__init__(n, a)
        self.score = s

    def infos(self):
        super().infos()
        # print("姓名:", self.name)
        # print("年龄:", self.age)
        print("成绩:", self.score)


s1 = Student('小张', 18, 100)
s1.infos()



# h1 = Human('小赵', 20)
# h1.infos()






