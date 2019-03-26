
# MySQL 概述
---

1. 什么是数据库
    - 存储数据的仓库
    
    
2. 都有哪些公司在用数据库
    - 金融机构、游戏网站、购物网站、论坛网站……
    

3. 提供数据库服务的软件
    - MySQL、Oracle、SQL Server、DB2、MongoDB、MariaDB
    - 如何选择使用那个数据库软件  
    
        1、是否开源
            - 开源：MySQL、MariaDB、MongoDB（游戏网站、购物网站、论坛网站）
            - 商业软件：Oracle、DB2、SQL Sever（政府部门、金融机构）
        2、是否跨平台
            - 不跨平台：SQL Server
            
            
4. MySQL的特点
    1. **关系型数据库**
        1. 关系型数据库特点
            1. 数据是以行和列（表格）的形式去存储的
            2. 表中的每一行叫做一条**记录**，每一列叫做一个**字段**
            3. 表和表之间的逻辑关联叫**关系**
            4. 关系型数据库的核心内容是**关系**即**二维表**    
        2. 示例
            1. 关系型数据库存储
                ```表1、学生信息表
                姓名    年龄    班级
                小明    25     三班
                小张    25     六班```
                
                ```表2、班级信息表
                班级    班主任
                三班    老李
                六班    老白```
            2. 非关系型数据库中存储 
                    {"姓名":"小明","年龄":25,"班级":"六班","班主任":"老李"}      
    2. **跨平台**  
        - 可以在Unix、Linux、Windows上运行数据库服务  
    3. **支持多种编程语言**
        - python、java、php……


5. 数据库软件、数据库、数据仓库的概念
    - 数据库软件
        - 一个软件、看得见、可操作、实现数据库的逻辑功能
    - 数据库
        - 一个逻辑概念，用来存放数据的仓库，侧重存储
    - 数据仓库
        - 从数据量来熟，比数据库庞大的多，主要用于数据分析和数据挖掘
    
    网购：
        - 数据库：user表
        - 数据仓库：那个时间段用户登录量最多……

# MySQL 安装

1. Ubuntu安装MqSQL服务
    1. 安装服务端  
            sudo apt-get install mysql-server
    2. 安装客户端  
            sudo apt-get install mysql-client  
    3. Ubuntu安装软件  
            sudo apt-get update 
            - 访问源列表中的每个网址，读取软件列表，保存到本地/var/lib/apy/lists/  
            sudo apt-get upgrade
            - 把本地已安装与刚下载的软件列表进行对比，如果发现已安装软件版本过低，则更新  
            sudo apt-get -f install 
            - 修复依赖关系
            
            
2. Windows安装MySQL服务


    1. 下载MySQL安装包（windows）
        - mysql-installerxxxx.msi


3. 启动和连接MySQL服务


    1. 服务端启动
    
        - 查看MySQL状态  
                sudo /etc/init.d/mysql status
                sudo /etc/init.d/mysql start stop restart
    2. 客户端连接
    
        - 命令格式  
                mysql -h主机地址 -u用户名 -p密码 
                mysql -hlocalhost -uroot -p123456（本地连接可省略h选项）

# 基本的SQL命令

## 使用规则

1. SQL每条命令必须以";"结尾
2. SQl命令不区分大小写
3. 使用 "\c" 来中止当前命令的执行

## macOS存放位置
- mac中添加环境：`PATH="$PATH":/usr/local/mysql/bin`
- 数据库目录：`/usr/local/mysql/data`

## Linux存放位置
- 数据库目录：`/var/lib/mysql`

## 库的管理

1. 库的基本操作
    - 查看已由库  
            show databases;
        
    - 创建库（指定字符集）  
            create database 库名 [character set utf8];
        
    - 查看创建库的语句（字符集）  
            show create database 库名
        
    - 查看当前所在库  
            select database();
        
    - 切换库  
            use 库名;
        
    - 查看库中已有表  
            show tables;
        
    - 删除库
            drop database 库名;
        
        
2. 库名的命名规则
    - 数字、字母、下划线，但不能使用纯数字
    - 库名区分字母大小写
    - 不能使用特殊关键字和mysql关键字

## 表的管理

1. 表的基本操作
    - 查看已有表  
            show tables;

    - 创建表（指定字符集）  
            create table 表名(
            字段名 数据类型,
            字段名 数据类型,
            ...          
            字段名 数据类型)character set utf8;
        
    - 查看已有表的字符集  
            show create table 表名;
        
    - 查看表结构  
            desc 表名
        
    - 删除表  
            drop table 表名;
        

## 表记录管理

1. insert 插入：
        - insert into 表名 values(值1),(值2),...;
        - insert into t1 values(1, 'Lucy', 90),(2, 'Green',86);
        - insetr into 表名(字段1,...) values(值1),...;
        - insert into t1(name,score) values('Peter',100); # id默认为空
        
2. select 查询：
        - select * from 表名 [where 条件];
        - select 字段1,字段2, from 表名 [where 条件];
        
        
3. alter 修改：        
        - 语法：
                alter table 表名 执行动作；
        - 添加字段(add)
                alter table 表名 add 字段名 数据类型;
                alter table 表名 add 字段名 数据类型 first;
                alter table 表名 add 字段名 数据类型 after 字段名;
        - 删除字段(drop)
                alter table 表名 drop 字段名;
        - 修改类型(modify)
                alter table 表名 modify 字段名 新数据类型;
        - 表重命名(rename)
                alter table 表名 rename 新表名;

        练习：
            1、查看所有库
            2、创建新库 studb
            3、在 studb 中创建表 tab1 ，指定字符集utf8，字段有id、name、age
            4、查看tab1的表结构
            5、在tab1中随便插入两条记录
            6、在tab2中的name、age两个字段插入两条记录
            7、查看tab1中所有记录
            8、查看tab1中所有人的姓名和年龄
            9、查看tab1表中年龄大于20的信息

## 如何更改默认字符集

- (Ubuntu)：
    - 获取root权限
            sudo i
            cd /etc/mysql/mysql.conf.d/
    - 备份
            cp mysqld.cnf mysqld.cnf.bak
    - subl mysqld.cnf
            [mysqld]
            character_set_sever = utf8
    - 重启mysql服务
            /etc/init.d/mysql restart
           

- (macOS):
        vim /etc/my.cnf
        [mysqld]
        character_set_server = utf8

## 数据类型
- 能存所有的，包括音频视频，但是一般存一个路径就好了

### 数值类型

1. 整型
    - int 大整型（4个字节）
        - 取值范围：2\*\*32-1(42亿多）
    - tinyint 微小整型（1个字节）
        - 有符号（signed默认）：-128～127
        - 无符号（unsigned）：0～255
        - 例如：age tinyint unsigned;
    - smallint 小整型（2个字节）
    - bigint 极大整型（8个字节）
        - 取值范围：2\*\*64-1
        
        
2. 浮点型        
    - float（4个字节，最多显示7个有效位）
        - 用法：
                字段名 float(m,n) m->总位数 n->小数位位数
                float(5,2)取值范围是：-999.99～999.99
    - decimal（最多显示28个有效位）
        - decimal(m,n)
        - 存储空间(整数、小树分开存储)
            - 规则：将9的倍数包装成4个字节
                    余数    字节
                     0       0
                    1-2      1
                    3-4      2
                    5-6      3
                    7-9      4
                    示例：decimal(19,9)
                        整数部分：10/9=1...1 4个字节+1个字节=5个字节
                        小数部分：9/9=1...0  4个字节+0个字节=4个字节
                        占：9字节

### 字符类型

1. char（定长）
    - 取值范围：1～255
    - name char(10) 会在后面加空格，始终是10个字符的大小
        - 浪费存储空间，但是效率高
    
    
2. varchar（变长）
    - 取值范围：1～65535
    - varchar(10) 会根据大小来开辟空间
        - 节省存储空间，但是效率低
        
        
3. text / longtext（4G） / blob / longblob（4G）
    
    
4. 注意：
    - 浮点型，插入整数时会自动补全小数位数
    - 小数位数多于指定位数，会对下一位进行四舍五入

---
- 数值类型宽度为显示宽度，只用于select查询显示，和占用内存无关，可用zerofill（用零填充）查看效果。


- 字符类型的宽度超过之后则无法存储 

### 枚举类型

1. 单选(enum)：
        字段名 enum(值1,值,2,...)
2. 多选(set)：
        字段名 set(值1,值,2,...)
        
        
        create table t5(
        id int(3) zerofill,
        name varchar(15),
        sex enum("M","F","Secret"),
        likes set("F","M","Study","Python")
        );
        
多选插入记录时要insert into t1(likes) values("F,Study,Python");

### 日期时间类型

1. date:"YYYY-MM-DD"
2. time:"HH:MM:SS"
3. datetime:"YYYY-MM-DD HH:MM:SS"
4. timestamp:"YYYY-MM-DD HH:MM:SS"
- datetime不给值默认返回NULL
- timestamp不给值默认返回系统时间

        create table t7(
        id int,
        name varchar(15),
        birthday date,
        money int,
        shijian datetime)
        
        insert into t7 values(1, "小明", 19900910, 5000, 20180731090000);
        

- 日期时间函数
        - now() 返回服务器当前时间
        - curdate() 返回当前日期
        - curtime() 返回当前时间
        - year(date) 返回指定时间的年份
        - date(date) 返回指定时间的日期
        - time(date) 返回指定时间的时刻
        
        `select * from t7 where date(shijian)='20180712';`
        `select * from t7 where date(shijian)>'20180712 and ....';`
        
- 日期时间的运算
        - select * from 表名 where 字段名 运算符(时间-interval 时间间隔单位);
        - 时间间隔单位：
            1 day/ 2 hour/ 1 minute/ 2 year/ 3 month
        
        1、查询1天以内的记录
            select * from t7
            where shijian > (now()-interval 1 day)
            
        2、查询一年以前的记录
            select * from t7
            where shijian < (now()-interval 1 year)
            
        3、查询1天以前，3天以内的记录
            select * from t7
            where shijian <(now()-interval 1 day) and
            where shijian >(now()-interval 3 day;
