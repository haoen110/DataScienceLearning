
from menu import show_menu
from student_info import *

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
        elif s == '5':
            print_by_score_desc(docs)
        elif s == '6':
            print_by_score_asc(docs)
        elif s == '7':
            print_by_age_desc(docs)
        elif s == '8':
            print_by_age_asc(docs)
        elif s == 'q':
            return  # 结束此函数执行，直接退出

main()
