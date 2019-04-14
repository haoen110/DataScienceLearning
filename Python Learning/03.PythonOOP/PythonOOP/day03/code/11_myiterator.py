# 11_myiterator.py


# 此示例示意可迭代对象和迭代器的定义及使用方式:
class MyList:
    def __init__(self, iterator):
        '''自定义列表类的初始化方法,此方法创建一个data实例
        变量来绑定一个用来存储数据的列表'''
        self.data = list(iterator)

    def __repr__(self):
        '''此方法了为打印此列表的数据'''
        return 'MyList(%r)' % self.data

    def __iter__(self):
        '''有此方法就是可迭代对象,但要求必须返回迭代器'''
        print("__iter__方法被调用!")
        return MyListIterator(self.data)

class MyListIterator:
    '''此类用来创建一个迭代器对象,用此迭代器对象可以迭代访问
    MyList类型的数据'''
    def __init__(self, iter_data):
        self.cur = 0  # 设置迭代器的初始值为0代表列表下标
        # it_data 绑定要迭代的列表
        self.it_data = iter_data

    def __next__(self):
        '''有此方法的对象才叫迭代器, 
        此方法一定要实现迭代器协议'''
        print("__next__方法被调用!")
        # 如果self.cur已经超出了列表的索引范围就报迭代结束
        if self.cur >= len(self.it_data):
            raise StopIteration
        # 否则尚未迭代完成,需要返回数据
        r = self.it_data[self.cur]  # 拿到要送回去的数
        self.cur += 1  # 将当前值向后移动一个单位
        return r

myl = MyList([2, 3, 5, 7])
print(myl)

for x in myl:
    print(x)  # 此处可以这样做吗?

# it = iter(myl)
# x = next(it)
# print(x)
# x = next(it)
# print(x)
# x = next(it)
# print(x)


