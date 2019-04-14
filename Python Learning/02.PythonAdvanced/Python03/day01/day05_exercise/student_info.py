# 4. 修改之前的学生信息管理程序，实现添加菜单和选择菜单操作功能:
#    菜单:
#      +-----------------------------+
#      |  1) 添加学生信息              |
#      |  2) 查看所有学生信息          |
#      |  3) 修改学生的成绩            |
#      |  4) 删除学生信息              |
#      |  q) 退出                     |
#      +-----------------------------+
#    请选择: 1
#      请输入姓名:....
#    请选择: 3
#      请输入修改学生的姓名: ....
#   (要求每个功能都对应一个函数)


def input_student():
    # 此函数获取学生信息，并返回学生信息的字典的列表
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

# 写一个打印菜单的函数
def show_menu():
    print('+-----------------------------+')
    print('|  1) 添加学生信息            |')
    print('|  2) 查看所有学生信息        |')
    print('|  3) 修改学生的成绩          |')
    print('|  4) 删除学生信息            |')
    print('|  q) 退出                    |')
    print('+-----------------------------+')

# 此函数用来存改学生的信息
def modify_student_info(lst):
    name = input("请输入要修改学生的姓名: ")
    for d in lst:
        if d['name'] == name:
            score = int(input("请输入新的成绩: "))
            d['score'] = score
            print("修改", name, '的成绩为', score)
            return
    else:
        print("没有找到名为:", name, '的学生信息')

# 定义一个删除学生信息的函数
def delete_student_info(lst):
    name = input("请输入要删除学生的姓名: ")
    for i in range(len(lst)):  # 从0开始把所有索引取出一遍
        if lst[i]['name'] == name:
            del lst[i]
            print("已成功删除: ", name)
            return True
    else:
        print("没有找到名为:", name, "的学生")

# 定义一个主函数，用来获取键盘操作，实现选择的功能
def main():
    docs = []  # 此列表用来存储所有学生的信息的字典
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':  # 修改学生成绩
            modify_student_info(docs)
        elif s == '4':  # 删除学生成绩
            delete_student_info(docs)
        elif s == 'q':
            return  # 结束此函数执行，直接退出


main()