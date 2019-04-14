# 08_number_trans.py



'''此示例示意自定义的类MyNumber能够转成为数值类型'''
class MyNumber:
    def __init__(self, v):
        self.data = v
    def __repr__(self):
        return "MyNumber(%d)" % self.data
    def __int__(self):
        '''此方法用于int(obj) 函数重载,必须返回整数
        此方法通常用于制订自义定对象如何转为整数的规则
        '''
        return 10000


n1 = MyNumber(100)
print(type(n1))
# if n1 == 100:
#     print("n1 == 100")
n  = int(n1)
print(type(n))
print(n)