# 10_override.py

# 此示例示意覆盖的用法

class A:
    def work(self):
        print("A.work()被调用")

class B(A):
    '''B类继承自A类'''
    def work(self):
        print("B.work()被调用")

b = B()
b.work()  # B.work()被调用
b.__class__.__base__.work(b)

a = A()
a.work()  # 请问结果是什么?






