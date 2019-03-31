# 09_mylist.py


# 自定义一个MyList类,与系统内建的类一样,
# 用来保存有先后顺序关系的数据

class MyList:
    '''自定义列表类'''
    def __init__(self, iterator=[]):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __abs__(self):
        # return MyList([abs(x) for x in self.data])
        # 上一句语句可以用如下生成表达式代替已防止过多占内存
        return MyList((abs(x) for x in self.data))

    def __len__(self):
        # return self.data.__len__()
        return len(self.data)

myl = MyList([1, -2, 3, -4])
print(myl)
print(abs(myl))  # MyList([1, +2, 3, +4])
print("原来的列表是:", myl)

myl2 = MyList(range(10))
print(myl2)
print('myl2的长度是:', len(myl2))
print('myl的长度是: ', len(myl))










