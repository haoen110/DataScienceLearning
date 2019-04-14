# 2. 修改之前的学生信息管理程序:
#   编写两个函数用于封装 录入学生信息 和 打印学生信 息的功能
#     1) 
#     def input_student():
#         #此函数获取学生信息，并返回学生信息的字典的列表
#         ....
#     2. 
#     def output_student(L):
#         # 以表格形式再打印学生信息
#         ...
#   验证测试：
#     L = input_studnet()
#     output_student(L)
#     print("再添加几个学生信息")
#     L += input_student()
#     print("添加学生后的学生信息如下:")
#     output_student(L)

def input_student():
    #此函数获取学生信息，并返回学生信息的字典的列表
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
    return L

def output_student(L):
    # 以表格形式再打印学生信息
    print('+------------+------+-------+')
    print('|   name     | age  | score |')
    print('+------------+------+-------+')
    for d in L:  # d绑定的是字典
        t = (d['name'].center(12),
             str(d['age']).center(6),
             str(d['score']).center(7))
        line = "|%s|%s|%s|" % t  # t是元组
        print(line)
    print('+------------+------+-------+')



L = input_student()
output_student(L)
print("再添加几个学生信息")
L += input_student()
print("添加学生后的学生信息如下:")
output_student(L)




