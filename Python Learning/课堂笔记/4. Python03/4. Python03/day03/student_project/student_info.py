# 3. 改写之前学生信息管理程序，添加如下四个功能
#   5)  按成绩从高至低打印学生信息
#   6)  按成绩从低至高打印学生信息
#   7)  按年龄从大到小打印学生信息
#   8)  按年龄从小到大打印学生信息
#   (要求原来输入的列表顺序保持不变)


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



#   5)  按成绩从高至低打印学生信息
def print_by_score_desc(lst):
    L = sorted(lst,
               key=lambda d: d['score'],
               reverse=True)
    output_student(L)


#   6)  按成绩从低至高打印学生信息
def print_by_score_asc(lst):
    L = sorted(lst,
               key=lambda d: d['score'])
    output_student(L)


#   7)  按年龄从大到小打印学生信息
def print_by_age_desc(lst):
    L = sorted(lst,
               key=lambda d: d['age'],
               reverse=True)
    output_student(L)


#   8)  按年龄从小到大打印学生信息
def print_by_age_asc(lst):
    L = sorted(lst,
               key=lambda d: d['age'])
    output_student(L)


