# 06_del_method.py

# 此示例示意__del__方法的用法

class Car:
    def __init__(self, name):
        self.name = name
        print('汽车', name, '对象已经创建!')

    def __del__(self):
        print(self.name, "对象已经销毁!")

c1 = Car('BYD E6')
# del c1
c1 = Car('BMW x5')

while True:  # 死循环阻止程序退出
    pass

