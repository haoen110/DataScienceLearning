"""
学生管理系统主模块

这个模块是操作的主模块
"""

from menu import *
from Student import *
from student_info import *

def main():
    L = []
    while True:
        show_menu1()
        s = input("请选择：")
        if s == '1':
            L += input_student()
        if s == '2':
            show_menu2()
            n = input("请选择：")
            if n == '1':
                output_student(L)
            if n == '2':
                L1 = sorted(L, key=lambda d: d.get_infos()[2], reverse=True)
                output_student(L1)
            if n == '3':
                L1 = sorted(L, key=lambda d: d.get_infos()[2])
                output_student(L1)
            if n == '4':
                L1 = sorted(L, key=lambda d: d.get_infos()[1], reverse=True)
                output_student(L1)
            if n == '5':
                L1 = sorted(L, key=lambda d: d.get_infos()[1])
                output_student(L1)
        if s == '3':
            output_student(L)
            alter_student(L)
        if s == '4':
            L = drop_student(L)
        if s == '5':
            save(L)
        if s == '6':
            L = load()
        if s == 'q':
            exit()
        s = input("操作完成，输入回车返回菜单：")


if __name__ == '__main__':
    main()
