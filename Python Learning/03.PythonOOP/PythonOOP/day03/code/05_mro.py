# 05_mro.py

# 此示例示意在多继承中的方法查找顺序问题

class A:
    def m(self):
        print("A.m")
class B(A):
    def m(self):
        print("B.m")
class C(A):
    def m(self):
        print("C.m")
class D(B, C):
    '''d类继承自B,C'''
    def m(self):
        print("D.m")
d = D()
# print(D.__mro__)
for x in D.__mro__:
    print(x)
d.m()  # 调用方法的顺序是什么?







