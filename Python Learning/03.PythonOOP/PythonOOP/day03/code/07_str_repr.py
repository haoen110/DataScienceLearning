# 07_str_repr.py


# 此示例示意一个自定义的数字类型重写 repr和 str的方法
class MyNumber:
    def __init__(self, value):
        self.data = value
    def __str__(self):
        print("__str__被调用")
        return "数字: %d" % self.data
    def __repr__(self):
        print("__repr__被调用")
        return 'MyNumber(%d)' % self.data

n1 = MyNumber(100)
# print(str(n1))  # 调用 n1.__str__(self)
# print(repr(n1))
print(n1)

# n2 = eval("MyNumber(100)")