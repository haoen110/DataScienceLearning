# 04_slots.py


# 此示例示意 类的变量 __slots__列表的作用
class Student:
    __slots__ = ['name', 'score']
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student('小张', 58)
print(s1.score)
# s1.socre = 100  # 此处错写了属性名,但在运行时不会报错!
s1.score = 100
print(s1.score)  # 请问打印的值是多少?