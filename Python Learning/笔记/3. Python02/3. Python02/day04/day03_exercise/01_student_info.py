# 2. 学生管理项目准备工作:
#    写一个程序，任意输入n个学生的信息,形成字典后存于列表中:
#      学生的信息包括:
#         姓名(字符串)
#         年龄(整数)
#         成绩(整数)
#    循环输入学生信息，直到输入学生姓名为空时结束输入,
#    最后形成字典列表如下:
#      L = [
#           {'name':'xiaozhang', 'age':20, 'score': 100},
#           {'name':'xiaoli', 'age':21, 'score': 98},
#           {'name':'xiaowang', 'age':19, 'score': 89},
#           ...
#      ]
#   2) 将以上列表显示为如下的表格:
#   +------------+------+-------+
#   |   name     | age  | score |
#   +------------+------+-------+
#   | xiaozhang  |  20  |  100  |
#   |  xiaoli    |  21  |   98  |
#   | xiaowang   |  19  |   89  |
#   +------------+------+-------+


# 第一步，读取学生信息，形成字典后存入列表L中
L = []
# d = {}  # 此处所有学生将共用一个字典，会出错
while True:
    name = input("请输入学生姓名: ")
    if not name:
        break
    age = int(input("请输入学生年龄: "))
    score = int(input("请输入学生成绩: "))
    d = {}  # 重新创建一个新的字典
    d['name'] = name
    d['age'] = age
    d['score'] = score
    L.append(d)

# print(L)
print('+------------+------+-------+')
print('|   name     | age  | score |')
print('+------------+------+-------+')
for d in L:  # d绑定的是字典
    t = (d['name'].center(12),
         str(d['age']).center(6),
         str(d['score']).center(7))
    line = "|%s|%s|%s|" % t  # t是元组
    print(line)

# print('| xiaozhang  |  20  |  100  |')
# print('|  xiaoli    |  21  |   98  |')
# print('| xiaowang   |  19  |   89  |')

print('+------------+------+-------+')
