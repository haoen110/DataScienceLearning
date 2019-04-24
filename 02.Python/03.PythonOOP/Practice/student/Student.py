# Student.py

class Student:
    count = 0 # 此类变量用来记录学生的个数
    
    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s
        Student.count += 1
    
    def __del__(self):
        Student.count -= 1

    def get_infos(self):
        return (self.__name, self.__age, self.__score)

    def set_score(self, score):
        '''此方法用于制定设置成绩时的规则'''
        if 0 <= score <= 100:
            self.__score = score
            return
        raise ValueError('不合法的成绩' + str(score))

    def set_age(self, age):
        '''此方法用于制定设置成绩时的规则'''
        if 0 <= age <= 150:
            self.__age = age
            return
        raise ValueError('不合法的年龄' + str(age))

    def is_name(self, n):
        '''判断n是否和self的名字相同'''
        return self.__name == n

    def write_to_file(self, file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write("\n")

    @classmethod
    def getTotalCount(cls):
        '''此方法用来得到学生对象的个数'''
        return cls.count