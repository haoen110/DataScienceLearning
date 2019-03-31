# 与Python交互

python3模块名：pymysql

`conda install pymysql`
`conda install sqlalchemy`

python2模块名：MySQLdb


```python
import pymysql

# 1、创建与数据库连接对象
db = pymysql.connect(host='localhost', user='haoen110', password='123', 
                     database='db4', charset='utf8')
# 2、利用db方法创建游标对象
cur = db.cursor()

# 3、利用游标对象execute()方法执行SQL命令
cur.execute("insert into sheng values\
            (16,300000,'台湾省');")

# 4、提交到数据库执行
db.commit()
print("OK!")

# 5、关闭游标对象
cur.close()

# 6、断开数据库连接
db.close()
```

    +----+--------+-----------+
    | id | s_id   | s_name    |
    +----+--------+-----------+
    |  1 | 130000 | 河北省    |
    |  2 | 140000 | 陕西省    |
    |  3 | 150000 | 四川省    |
    |  4 | 160000 | 广东省    |
    |  5 | 170000 | 山东省    |
    |  6 | 180000 | 湖北省    |
    |  7 | 190000 | 河南省    |
    |  8 | 200000 | 海南省    |
    |  9 | 200001 | 云南省    |
    | 10 | 200002 | 山西省    |
    | 16 | 300000 | 台湾省    |
    +----+--------+-----------+

## pymysql 使用流程

1、建立数据库连接`db = pymysql.connect(...)`  
2、创建游标对象`cur = db.cursor()`    
3、游标方法`cur.execute("insert ...")`  
4、提交到数据库`db.commit()`       
5、关闭游标对象`cur.close()`  
6、断开数据库连接`db.close()`  

### connect对象
- 建立数据库连接`db = pymysql.connect(...)`  
    - host:主机地址，本地 localhost
    - port:端口号，默认3306  
    - user:用户名
    - password:密码
    - database:库
    - charset:编码方式，推荐使用utf8

### 数据库连接对象(db)的方法
- `db.close()` 关闭连接
- `db.commit()` 提交到数据库执行
- `db.rollback()` 回滚
- `cur = db.cursor()` 返回游标对象，用于执行SQL具体SQL命令

### 游标对象(cur)的方法
- 创建游标对象`cur = db.cursor()`
    - `cur.execute(SQL命令,[列表])` 执行SQL命令
    - `cur.close()` 关闭游标对象
    - `cur.fetchone()` 获取第一条数据
        - 是一个元组(1,100001,"河北省")
    - `cur.fetchone()` 获取第一条数据
    - `cur.fetchmany(n)` 获取n条数据
    - `cur.fetchall()` 获取所有记录
        


```python
import pymysql

# 1、创建与数据库连接对象
db = pymysql.connect(host='localhost', user='haoen110', password='123', 
                     database='db4', charset='utf8')
# 2、利用db方法创建游标对象
cur = db.cursor()

# 3、利用游标对象execute()方法执行SQL命令
try:
    sql_select = "select * from sheng"
    cur.execute(sql_select)
    
    data1 = cur.fetchone()
    print(data1)
    print("*"*10)
    
    data2 = cur.fetchmany(3)
    for m in data2:
        print(m)
    print("*"*10)
    
    data3 = cur.fetchall()
    for m in data3:
        print(m)
    print("*"*10)
    
except Exception as e:
    db.rollback()
    print("出现错误，已回滚", e)
    
# 4、提交到数据库执行
db.commit()
print("OK!")

# 5、关闭游标对象
cur.close()

# 6、断开数据库连接
db.close()
```

    (1, 130000, '河北省')
    **********
    (2, 140000, '陕西省')
    (3, 150000, '四川省')
    (4, 160000, '广东省')
    **********
    (5, 170000, '山东省')
    (6, 180000, '湖北省')
    (7, 190000, '河南省')
    (8, 200000, '海南省')
    (9, 200001, '云南省')
    (10, 200002, '山西省')
    (16, 300000, '台湾省')
    **********
    OK!


### 参数化


```python
# 插入数据
import pymysql

# 1、创建与数据库连接对象
db = pymysql.connect(host='localhost', user='haoen110', password='123', 
                     database='db4', charset='utf8')
# 2、利用db方法创建游标对象
cur = db.cursor()

# 3、利用游标对象execute()方法执行SQL命令

s_id = input("请输入省的编号：")
name = input("请输入省的名字：")

try:
    sql_insert = "insert into sheng(s_id,s_name) values(%s,%s);"
    cur.execute(sql_insert, [s_id, name])
    print("插入成功！")

except Exception as e:
    db.rollback()
    print("出现错误，已回滚", e)
    
# 4、提交到数据库执行
db.commit()
print("OK!")

# 5、关闭游标对象
cur.close()

# 6、断开数据库连接
db.close()
```

    请输入省的编号：999
    请输入省的名字：haha
    插入成功！
    OK!


    +----+--------+-----------+
    | id | s_id   | s_name    |
    +----+--------+-----------+
    |  1 | 130000 | 河北省    |
    |  2 | 140000 | 陕西省    |
    |  3 | 150000 | 四川省    |
    |  4 | 160000 | 广东省    |
    |  5 | 170000 | 山东省    |
    |  6 | 180000 | 湖北省    |
    |  7 | 190000 | 河南省    |
    |  8 | 200000 | 海南省    |
    |  9 | 200001 | 云南省    |
    | 10 | 200002 | 山西省    |
    | 16 | 300000 | 台湾省    |
    | 17 |    999 | haha      |
    +----+--------+-----------+

## 自己写封装


```python
from pymysql import *

class Mysqlpython:
    def __init__(self, database, host='localhost',
                 user='haoen110', password='123', 
                 port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.database = database
    
    def open(self):
        self.db = connect(host=self.host,
                          user=self.user,
                          port=self.port,
                          database=self.database,
                          password=self.password,
                          charset=self.charset)
        self.cur = self.db.cursor()
        
    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,L=[]):    # pymysql.execute(sql)
        try:
            self.open()
            self.cur.execute(sql,L)
            self.db.commit()
            print("ok")
        except Exception as e:
            self.db.rollback()
            print("Failed",e)
        self.close()


    def all(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("Failed",e)
        self.close()
        
# 创建数据库连接对象
# sqlh = Mysqlpython("db4")
# sql_insert = "insert into sheng(s_id,s_name) values(666,'jjj');"
# sqlh.zhixing(sql_insert)

sql_select = "select * from sheng;"
data = sqlh.all(sql_select)
print(data)
```

    ok
    ((1, 130000, '河北省'), (2, 140000, '陕西省'), (3, 150000, '四川省'), (4, 160000, '广东省'), (5, 170000, '山东省'), (6, 180000, '湖北省'), (7, 190000, '河南省'), (8, 200000, '海南省'), (9, 200001, '云南省'), (10, 200002, '山西省'), (16, 300000, '台湾省'), (17, 999, 'haha'), (18, 666, 'jjj'))


## 自制登录系统

```
create table user(
username varchar(20),
password char(40)
);

insert into user values("SHE","7c4a8d09ca3762af61e59520943dc26494f8941b"); # sha1加密的123456
```


```python
from hashlib import sha1

uname = input("请输入用户名：")
pwd = input("请输入密码：")

# 用sha1给pwd加密
s1 = sha1() # 创建sha1加密对象
s1.update(pwd.encode("utf8"))  # 指定编码
pwd2 = s1.hexdigest() # 返回16进制加密的结果

sqlh = Mysqlpython("db4")
select = "select password from user where username=%s;"
result = sqlh.all(select,[uname])

print(result) # 打印出来看看

if len(result) == 0:
    print("用户名不存在")
elif result[0][0] == pwd2:
    print("登录成功")
else:
    print("密码错误")

```

    请输入用户名：SHE
    请输入密码：123456
    (('7c4a8d09ca3762af61e59520943dc26494f8941b',),)
    登录成功


# ORM (Object Relation Mapping 对象关系映射)

- 定义：
    - 把对象模型映射到MySQL数据库中
   
   
- sqlalchemy模块安装
    - 示例：

            class User(Base):
                __tablename__="t1" # 声明要创建的表名
                id = Column(Integer, primary+key=True)
                name = Column(String(20))
            # 解释：User 一张表，id name


```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql://haoen110:123@localhost/db4",encoding="utf8")
Base = declarative_base() # orm基类

class User(Base): # 继承Base基类
    __tablename__ = "t123"
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    address = Column(String(40))

Base.metadata.create_all(engine)
```

    +---------+-------------+------+-----+---------+----------------+
    | Field   | Type        | Null | Key | Default | Extra          |
    +---------+-------------+------+-----+---------+----------------+
    | id      | int(11)     | NO   | PRI | NULL    | auto_increment |
    | name    | varchar(20) | YES  |     | NULL    |                |
    | address | varchar(40) | YES  |     | NULL    |                |
    +---------+-------------+------+-----+---------+----------------+
