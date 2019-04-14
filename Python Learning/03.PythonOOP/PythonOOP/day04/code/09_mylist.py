


# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __neg__(self):
        '''此方法用来制定 - self 返回的规则'''
        # L = [-x for x in self.data]
        L = (-x for x in self.data)
        return MyList(L)

L1 = MyList([1, -2, 3, -4])
L2 = -L1
print(L2)


