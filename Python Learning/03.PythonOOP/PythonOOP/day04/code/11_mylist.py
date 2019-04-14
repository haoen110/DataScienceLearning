# 此示例示意  [] 运算符的重载
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        # if type(i) is not int:
        #     raise TypeError
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v =', v)
        self.data[i] = v  # 修改data绑定的列表


L1 = MyList([1, -2, 3, -4])
v = L1[-1]
print(v)

L1[1] = 2  # 等同于调用 L1.__setitem__(1, 2)
print(L1)

# 以下操作会出错
# print(L1[100000000000])
# print(L1['hello'])
