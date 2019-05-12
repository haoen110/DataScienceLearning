
https://nb.anjuke.com/sale/gaoxinquz/p1/

import pymysql
import getpass
import warnings

# 创建数据库连接对象
db = pymysql.connect("localhost", "root", getpass.getpass("请输入root用户密码："))

# 创建游标对象
cursor = db.cursor()

# 执行语句
# 过滤警告
warnings.filterwarnings("ignore") # 出现警告时的做法
try:
    cursor.execute("create database if not exists spiderdb")
    cursor.execute("use spiderdb")
    cursor.execute("create table if not exists t1(id int)")
except Warning:
    pass

sql = "insert into t1 values(%s)"
cursor.execute(sql, [1])
cursor.execute(sql, [2])

# 提交
db.commit()

# 关闭
cursor.close()
db.close()