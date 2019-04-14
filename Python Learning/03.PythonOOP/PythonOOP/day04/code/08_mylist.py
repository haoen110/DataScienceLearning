


# 此示例示意复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.data = list(iterable)

    def __add__(self, rhs):
        print('__add__被调用')
        return MyList(self.data + rhs.data)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __iadd__(self, rhs):
        print("__iadd__被调用！！！！")
        self.data.extend(rhs.data)
        return self

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L1 += L2  # 当没有__iadd__方法时，等同于调用L1 = L1 + L2
print(L1)


