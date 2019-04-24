"""
学生类
"""


class Student:
    count = 0  # 此，类变量，用来记录学生的个数

    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s
        Student.count += 1

    def __del__(self):
        Student.count -= 1

    def get_infos(self):
        return self.__name, self.__age, self.__score

    def alter_infos(self, age=-1, score=-1):
        if age != -1:
            self.__age = age
        if score != -1:
            self.__score = score
