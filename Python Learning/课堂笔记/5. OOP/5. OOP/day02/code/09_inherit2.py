# 09_inherit.py


# 此示例示意继承和派生
class Human(object):
    '''此类用来描述人类的共性行为'''
    def say(self, that):  # 说话
        print("say:", that)
    def walk(self, distance):  # 走路
        print("走了", distance, '公里')


class Student(Human):
    def study(self, subject):
        print("正在学习", subject)


class Teacher(Student):
    def teach(self, subject):
        print("正在教:", subject)



h1 = Human()
h1.say('今天天气真热')
h1.walk(5)

print('-------以下是学生对象的行为-----------')
s1 = Student()
s1.say('学习有点累')
s1.walk(3)
s1.study('python')


t1 = Teacher()
t1.say('明天就星期六了')
t1.walk(6)
t1.teach('面向对象')
t1.study('钢琴')


