# 07_object_relative.py

# 有两个人:
#   1.
#     姓名: 张三
#     年龄: 35
#   2.
#     姓名: 李四
#     年龄: 8
#   行为:
#     1. 教别人学东西 teach
#     2. 赚钱
#     3. 借钱
# 事情:
#    张三 教 李四 学 python
#    李四 教 张三 学 跳皮筋
#    张三 上班赚了 1000元钱
#    李四向张三借了 200元


# 此示例示意如何用面向对象的方式创建对象,
# 并建立对象与对象之间的逻辑关系

class Human:
    '''人类,用于描述人的行为和属性'''
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 钱数为0

    def teach(self, other, skill):
        print(self.name, "教", other.name,
              '学', skill)

    def works(self, money):
        self.money += money
        print(self.name, '工作赚了', money, '元钱')

    def borrow(self, other, money):
        '描述一个人向其它人借钱的行为,它人有钱必借,不够不借'
        if other.money > money:
            print(other.name, "借给", self.name,
                money, '元钱')
            other.money -= money
            self.money += money
        else:
            print(other.name, '不借给', self.name)

    def show_info(self):
        print(self.age, '岁的', self.name,
            '存有', self.money, '元线')

# 以下的类的使用
zhang3 = Human('张三', 35)
li4 = Human('李四', 8)
zhang3.teach(li4, 'Python')
li4.teach(zhang3, '跳皮筋')
zhang3.works(1000)
li4.borrow(zhang3, 200)
zhang3.show_info()
li4.show_info()



