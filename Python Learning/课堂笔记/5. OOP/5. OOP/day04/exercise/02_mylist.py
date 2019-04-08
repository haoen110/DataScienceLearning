# 实现两个自定义列表相加:
#   class MyList:
#       def __init__(self, iterable):
#           self.data = list(iterable)
#       .... 以下自己实现

#   L1 = MyList([1, 2, 3])
#   L2 = MyList([4, 5, 6])
#   L3 = L1 + L2
#   print(L3)  # MyList([1,2,3,4,5,6])
#   L4 = L2 + L1
#   print(L4)  # MyList([4,5,6,1,2,3])
#   L5 = L1 * 2
#   print(L5)  # MyList([1,2,3,1,2,3])



class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __mul__(self, rhs):  # rhs 绑定整数
        return MyList(self.data * rhs)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2  # 等同于L1.__add__(L2)
print(L3)  # MyList([1,2,3,4,5,6])
L4 = L2 + L1  # 等同于L2.__add__(L1)
print(L4)  # MyList([4,5,6,1,2,3])
L5 = L1 * 2  # L1.__mul__(2)
print(L5)  # MyList([1,2,3,1,2,3])

# 问题?  以下错误的解决办法必须是反向运算符的重载
# L6 = 2 * L1  # 2.__mul__(L1)
# print(L6)