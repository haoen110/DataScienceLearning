import pymysql
import re

f = open('dict.txt')
pw = input("请输入root用户密码：")
db = pymysql.connect('localhost', 'root', pw, 'dict')

cursor = db.cursor()

for line in f:
    l = re.split(r'\s+', line) # \s表示匹配任意空字符 + 表示匹配前面的字符出现1次或多次
    word = l[0]
    interpret = ' '.join(l[1:])
    sql = "insert into words (word,interpret) values ('{}', '{}')".format(word, interpret)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

f.close()
