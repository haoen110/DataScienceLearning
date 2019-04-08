# 05_classmethod.py


# 此示例示意类方法的定义方法和用法
class Car:
    count = 0  # 类变量

    @classmethod
    def getInfo(cls):
        return cls.count

c1 = Car()  # 创建一个对象
c1.count = 100
v = c1.getInfo()  # 0/100
print(v)

