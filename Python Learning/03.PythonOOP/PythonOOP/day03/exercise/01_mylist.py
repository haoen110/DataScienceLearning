# 练习:
#   已知list 列表类中没有insert_head方法,
#     写一个自定义的类MyList,继承自list类,在MyList类内添加

#     class MyList(list):
#       def insert_head(self, value):
#           '''以下自己实现,将Value插入到列表的开始处'''

#     如:
#       L = MyList(range(1,5))
#       print(L)  # [1,2,3,4]
#       L.insert_head(0)
#       print(L)  # [0,1,2,3,4]
#       L.append(5)
#       print(L)  # [0,1,2,3,4,5]


class MyList(list):
    def insert_head(self, value):
        '''以下自己实现,将Value插入到列表的开始处'''
        self.insert(0, value)


L = MyList(range(1, 5))
print(L)  # [1,2,3,4]
L.insert_head(0)
print(L)  # [0,1,2,3,4]
L.append(5)
print(L)  # [0,1,2,3,4,5]
