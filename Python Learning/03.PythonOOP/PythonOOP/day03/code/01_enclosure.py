# 01_enclosure.py


# 此示例示意使用私有属性和私有方法:
class A:
    def __init__(self):
        self.__p1 = 100  #__p1为私有属性,在类的外部不可访问

    def test(self):
        print(self.__p1)  # 可以访问
        self.__m1()  # A类的方法可以调用A类的私有方法

    def __m1(self):
        '''我是私有方法,只有我自己的类中的方法才能调用我哦'''
        print("我是A类的__m1方法!")

a = A()  # 创建对象
# print(a.__p1)  # 在类外看不到__p1属性,访问失败!
a.test()
# a.__m1()  # 出错.无法调用私有方法
