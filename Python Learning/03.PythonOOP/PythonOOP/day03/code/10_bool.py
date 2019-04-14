# 10_bool.py



class MyList:
    '''自定义列表类'''
    def __init__(self, iterator=[]):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "MyList(%r)" % self.data

    def __bool__(self):
        print("__bool__方法被调用!")
        return False

    # def __len__(self):
    #     print("__len__被调用")
    #     return len(self.data)

myl = MyList([1, -2, 3, -4])
print(bool(myl))  # True
if myl:
    print("myl 是真值")
else:
    print("myl 是假值")





