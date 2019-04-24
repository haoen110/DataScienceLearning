"""
学生信息相关操作
"""

from Student import *


def input_student():
    L = []
    while True:
        s = input("请输入学生的姓名、年龄、成绩，用空格隔开，输入为空时结束：")
        if not s:
            break
        name = s.split()[0]
        age = s.split()[1]
        score = s.split()[2]
        L.append(Student(name, int(age), int(score)))
    return L


def output_student(L):
    for i in L:
        name = i.get_infos()[0]
        age = i.get_infos()[1]
        score = i.get_infos()[2]
        print(name, age, score)


def alter_student(L):
    s = input("请输入要修改的学生姓名：")
    for i in L:
        if i.get_infos()[0] == s:
            s = int(input("要修改年龄请输入1，要修改年龄请输入2，两者都修改请输入3："))
            if s == 1:
                age = int(input("请输入最终的年龄："))
                i.alter_infos(age=age)
            if s == 2:
                score = int(input("请输入最终成绩："))
                i.alter_infos(score=score)
            if s == 3:
                age, score = input("请输入年龄和成绩，用空格隔开：").split()
                i.alter_infos(age=age, score=score)


def drop_student(L):
    s = input("请输入要删除的学生姓名：")
    L1 = []
    for i in L:
        if i.get_infos()[0] != s:
            L1.append(i)
    return L1


def save(L):
    f = open('db.txt', 'w')
    n = 0
    for i in L:
        name = i.get_infos()[0]
        age = i.get_infos()[1]
        score = i.get_infos()[2]
        if n == len(L) - 1:
            f.writelines([name, ',', age, ',', score])
        else:
            f.writelines([name, ',', age, ',', score, '\n'])
        n += 1
    f.close()


def load():
    f = open('db.txt')
    L = []
    for i in f:
        L1 = i.rstrip().split(',')
        name = L1[0]
        age = L1[1]
        score = L1[2]
        L.append(Student(name, int(age), (score)))
    f.close()
    return L
