# 10_contains.py


# 此示例示意in / not in 运算符的重载
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __contains__(self, e):
        '''此方法用来实现 in　/ not in 运算符的重载'''
        print("__contains__被调用")
        for x in self.data:
            if x == e:
                return True
        return False


L1 = MyList([1, -2, 3, -4])
if -2 in L1:
    print('-2 在 L1 中')
else:
    print('-2 不在 L1中')


# 当MyList的类内重载了__contains__方法，则not in也同时可用
if -3 not in L1:
    print("-3 不在 L1中")
else:
    print('-3 在 L2中')




