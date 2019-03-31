


# 此示例示意反向算术运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __mul__(self, rhs):  # rhs 绑定整数
        print('__mul__被调用')
        return MyList(self.data * rhs)
    def __rmul__(self, lhs):
        print('__rmul__被调用')
        return MyList(self.data * lhs)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L5 = L1 * 2  # L1.__mul__(2)
print(L5)  # MyList([1,2,3,1,2,3])

L6 = 2 * L1  # 2.__mul__(L1)
print(L6)