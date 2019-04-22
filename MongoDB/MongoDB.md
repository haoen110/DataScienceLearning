
# MongoDB

# 数据存储阶段

## 文件管理阶段（.txt  .doc .xls）

- 优点：
    - 使用简单，展现直观
    - 可以长期保存数据
    - 可存储数据量比较大

- 缺点：
    - 查找不方便
    - 容易造成数据冗余
    - 数据格式不规范
    
## 数据库管理阶段

- 优点：
    - 将数据结构化存储，降低冗余
    - 提高了增删改查效率
    - 方便扩展，方便程序调用
- 缺点：
    - 数据库往往需要指令或语句操作，相对复杂
- 概念：
    - 数据：能够输入到计算机中并被识别处理的信息的集合
    - 数据结构：组成一个数据集合的数据之间的关系
    - 数据库：按照一定的数据结构，存储数据的仓库。数据库是在数据库管理系统管理和控制下，在一定介质上的数据集合
    - 数据库管理系统：数据库管理软件，用于建立维护操作数据库
    - 数据库系统：由数据库和数据库管理系统高等开发工具组成的集合


### 关系型数据库

- *采用关系模型（二维表）来组织数据结构的数据库*
    - 例如：Oracle、DB2、SQLServer、Mysql、SQLite
- 优点：
    - 容易理解，逻辑类似常见的表格
    - 使用方便，都使用sql语句，sql语句非常成熟
    - 数据一致性高，冗余低，数据完整性好，便于操作
    - 技术成熟，功能强大，支持很多复杂操作
- 缺点：
    * 每次操作都要进行sql语句解析，消耗较大
    * 能很好的满足并发需求，特别是海量数据爆发，关系型数据库读写能力会显得不足
    * 关系型数据库往往每一步都要进行加锁的操作，也造成了数据库的负担
    * 数据一致性高，有时也会使数据的存储不灵活

### 非关系型数据库（NoSql（not  only  sql））

- 优点：
    - 高并发，读写能力强
    - 弱化数据结构一致性，使用更加灵活
    - 有良好的可扩展性
- 缺点：
    - 通用性差，没有sql语句那样同于的语句
    - 操作灵活导致容易出错和混乱
    - 没有外键关联等复杂的操作
- Nosql的使用情况
    1. 对数据存储灵活性要求高，一致性要求低
    2. 数据处理海量并发，要求瞬间效率速度比较高
    3. 数据比较容易建立Nosql模型
    4. 网站临时缓冲存储，爬虫应用
- Nosql分类
    1. 键值型数据库  Redis
    2. 文档型数据库  MongoDB
    3. 列存储数据库  HBase
    4. 图形数据库

# MongoDB数据库

- 非关系型数据库>文档型数据库>最像关系型的非关系型数据库
- 特点 ：
    1. 是由c++编写的数据库管理系统
    2. 支持丰富的数据操作，增删改查索引聚合
    3. 支持丰富的数据类型
    4. 使用方便，可以很好的扩展。相对比较成熟
    5. 支持众多的编程语言接口（python  PHP c++  c#）
- 要求：
    1. 关系型数据库和非关系型数据库各自有什么特点
    2. MongoDB是一个什么样的数据库

## MongoDB的安装

### 自动安装

`sudo apt-get install mongodb`
- 默认安装位置：`/var/lib/mongodb`或`/usr/local/var/mongodb`
- 配置文件位置：`/etc/mongodb.conf`或`/usr/local/etc/mongodb.conf`
- 命令集：`/usr/bin`或`/usr/local/bin`
- mac：brew services start mongodb


### 手动安装
1. 下载安装包：`www.mongodb.com`
2. 解压安装包：`/usr/local/`
3. 将解压后的MongoDB文件夹中的bin目录添加到环境比变量
    - `PATH=$PAHT:/opt/mongo...../bin
    export PATH```将以上两句写入启动脚本`/etc/rc.local`
4. 重启

# Mongodb 命令

- 设置数据库存储位置
    - `mongod --dbpath`目录
- e.g.  将存储路径设置为dbs
    - `mongod --dbpath  dbs` 
- 设置数据库监听端口
    - `mongod --port  8080`
- 默认监听端口27017

## 进入数据库交互操作界面

- `mongo shell`：
    - 用来操作mongodb数据库的界面，在这里可以使用mongo语句操作数据库内容
- `quit()``exit``ctrl-c`：
    - 退出
- 组织结构：键值对>文档>集合>数据库

    ---------------------------------
     ID   |   NAME   |   AGE
    ---------------------------------
     1    |   Lily   |   17
    ---------------------------------
     2    |   Lucy   |   18
    ---------------------------------

    {
      "ID":1,	
      "NAME":'Lily',
      "AGE":17
    },
    {
      "ID":2,	
      "NAME":'Lucy',
      "AGE":18
    }

## mysql 和 mongodb 概念对比

    mysql        mongodb         含义

    database     database       数据库

    table        collection     表/集合

    column       field          字段/域

    row          document       记录/文档

    index        index          索引

- 三个表
1. 用户信息      1
2. 朋友圈内容   多       多
3. 其他用户点赞，评论    多

    {id:xxx,name:'zhan',age:12,pyq:[{date:xxx,conten:xxx,image:[1,2,3],zan:[id1,id2],pl:[{date:xxx,con:xxx},{},{}]},{},{}]}

# 创建数据库
- `use  databaseName`
- e.g.  创建一个名字为stu的数据库
    - `use stu`
* use实际为选择使用哪个数据库，当数据库不存在时会自动创建
* use后并不会立即创建出数据库，而是需要等到插入数据时数据库才会创建

>数据库命名规则
1. 使用utf-8字符 （mongo默认支持utf-8）
2. 不能含有空格  .  /  \   '\0' 字符
3. 长度不超过64字节
4. 不能和系统数据库重名


## 查看系统中的数据库
- `show dbs`
- 系统数据库说明
    - admin ： 存储用户信息
    - local ： 存储本地数据
    - config ： 存储分片信息
- db：mongodb的全局量，代表当前正在使用的数据库
- 如果不选择使用任何数据库db代表test，直接插入数据就会建立test数据库

## 删除数据库
`db.dropDatabase()`:删除db所代表的数据库

## 数据库的备份和恢复

- 备份  
    - `mongodump  -h host  -d  dbname -o  bak`
        - e.g. 将本机test数据库备份到bak目录下
            - `mongodump -h 127.0.0.1 -d test -o bak`
- 恢复  
    - `mongorestore  -h  dbhost:port -d  dbname path`
        - e.g. 将test数据库恢复到本机的res数据库中（res不存在自动创建）
            - `mongorestore -h 127.0.0.1:27017 -d res  bak/test`
            
## 数据库的监测
`mongostat`：监测数据库运行数据

      insert query update delete ： 每秒增查改删的次数
      flushes  每秒和磁盘交互次数
      vsize    虚拟内存
      res      物理内存
      time     时间
 
`mongotop`：监控数据库读写时长

      ns  数据表
      total  总时间
      read   读时间
      write  写时间  

# 集合

## 创建集合
>集合命名规则
1. 合法的UTF-8字符
2. 不能有‘\0’
3. 不能以system.开头，因为这是系统保留集合前缀 
4. 不能和关键字重名

### 方法1
- `db.createCollection(collection_name)`
    - e.g. 创建class1集合
        - `db.createCollection('class1')`
        
### 方法2
- 当向一个集合中插入数据的时候如果集合不存在则自动创建
    - `db.collection_name.insert(...)`
    
### 查看集合
- `show collections`
- `show tables`

### 删除集合
- `db.collection.drop()`
    - `db.class2.drop()`删除class2集合：

### 集合重命名
- `db.collection.renameCollection("new_name")`
    - `db.class.renameCollection("class0")`将class集合重命名为 class0




# 文档
- mongodb中数据的组织形式
- mongodb文档：是以键值对的形成组成的一组数据。类似python中字典描述数据的方式
    - 键：即文档的域，表达了一个键值对的含义
            键的命名规则：
            1. utf-8格式字符串
            2. 不能使用‘\0’
            3. 一个文档中的键不能重复
    - 值：即文档存储的数据。


1. 文档中键值对是有序的
2. 文档中键值对严格区分大小写

    类型                  值

    整型                 整数 1  2   3
    布尔类型              true  false
    浮点型               小数

    Array               数组

    Date                时间日期
    Timestamp           时间戳

    String              字符串
    Symbol              特殊字符串
    Binary data         二进制子串

    Null                null 空值
    Object              内部文档（对象）
    code                js代码
    regex               正则子串
    ObjectId            自动生成ID标记

"_id" : ObjectId("5ba07671b17d2b40342f7c5c")

_id : 当mongodb插入文档时如果不指定_id域则自动生成_id域。值如果不自己指定即会自动生成一个ObjectId值

24位16进制  使用ObjectId经过算法处理保证其唯一性

5ba07671b17d2b40342f7c5c  
8位文档创建时间  6位  机器ID   4位进程id  6位计数器


## 集合中的文档

- 集合中的文档不一定有相同的域 
    - 个数不同
    - 域不相同
    - 数据类型不同
- 集合中文档各自比较独立，相互并不影响

## 集合创建原则
  1. 集合中的文档要描述**同一类事物**
  2. 数据库中同一类数据尽量集中存放在**相同的集合**
  3. 集合中的文档**嵌套层数**不要太多

## 插入文档
- `db.collection.insert()`
    - 功能：插入一个文档
    - 参数：要插入的文档

### 插入单个文档
- `db.class0.insert({'name':'Lucy',"age":18,"sex":'w'})`
- `db.class0.insert({_id:1,name:'Jame',age:16,sex:'m'})`

>插入操作中键可以不加引号  
查看插入结果 db.class0.find()  
_id 值可以自己插入，但是不能重复

### 插入多条文档
- 插入多条文档时，参数用中括号里面放入多个文档
- `db.class0.insert([{name:"Alex",age:19,sex:'m'},{name:'Abby',age:18,sex:'w'}])`

### 其他插入方法
- `insertOne()`插入一条文档
    - `db.class0.insertOne({name:"Levi",age:20,sex:'m'})`
- `insertMany()`插入多条文档
    - `db.class0.insertMany([{name:"John",age:16,sex:'m'},{name:"Lenzer",age:17,sex:'m'}])`
    
### save插入文档
- `db.collection.save()`
    - 如果正常插入与insert用法相同
        - `db.class0.save({name:'Allen',age:19,sex:'m'})`
        - `db.class0.save([{name:"Sunny",age:17,sex:'w'},{name:'Alice',age:16,sex:'w'}])`
    - 如果插入数据是有_id域，且_id域值存在时则会修改原有文档，如果该值不存在则正常插入
        - `db.class0.save({_id:2,name:'Mary',age:20,sex:'w'})`

### 获取集合对象方法
`db.class0`相当于`db.getCollection('class0')`  
`db.getCollection("class0").find()`

### 查找所有内容
`db.collection.find(query,field)`

`find(query,field)`
- 功能 ： 查找文档
- 参数 ： 
    - query ： 查找条件，相当于where子句，以键值对方式传递参数，如果是空{}表示查找所有内容
        - `db.class0.find({sex:'w'})`查找所有性别为w的文档  
    - field ： 查找的域，以键值对的方式给出要查找（不查找）的域以域名为键，以0,1为值分别表示不查找和查找
        - `db.class0.find({sex:'w'},{name:1,age:1})`查找所有性别为w的文档 
             * 如果某一个或多个域设置为0 表示这些域不查找，其他域均查找
             * 如果某一个或多个域设置为1 表示这些域查找，其他域均不查找
             * _id 除非设置为0 否则均会查找
             * 除_id域其他域不能有的设置1有的设置0
             
             
- 获取查找结果中的第3项
    - `db.class0.find({},{_id:0})[2] `         

`findOne(query,field)`
- 功能 ： 查找第一条符合条件的文档
- 参数 ： 同find
  - `db.class0.findOne({sex:'w'},{_id:0,name:1})`查找集合中性别为女的第一个文档

## 比较操作符

`$eq` 等于 == 
 
- 查找年龄等于18
    - `db.class0.find({age:{$eq:18}},{_id:0})`等同于`db.class0.find({age:18},{_id:0})`

`$lt` 小于  < 
- 查找年龄小于18的
    - `db.class0.find({age:{$lt:18}},{_id:0})`
    - `db.class0.find({name:{$lt:"John"}},{_id:0})`
        * 在mongodb中字符串可以比较大小

`$lte`  小于等于  <= 
- 年龄小于等于18 
    -`db.class0.find({age:{$lte:18}},{_id:0})`

`$gt`  大于  >
- 查找年龄大于16 且 小于19
    - `db.class0.find({age:{$gt:16,$lt:19}},{_id:0})`
        * 在mongodb中所有的{} [] 中都可以写多个条件。但根据参数的不同表达的意思不一样

`$gte` 大于等于 >= 
- 大于等于19
    `db.class0.find({age:{$gte:19}},{_id:0})`

`$ne`  不等于  !=
- 性别不等于‘m’的 
    - `db.class0.find({sex:{$ne:'m'}},{_id:0})`
        * 使用ne查找也会找到该域不存在的文档

`$in`  包含
- 找到年龄为 [10,20,30]
    - `db.class0.find({age:{$in:[10,20,30]}},{_id:0})`

`$nin` 不包含
- 找到年龄不是 17  18   19 的
    - ·db.class0.find({age:{$nin:[17,18,19]}},{_id:0})·

## 逻辑操作符

`$and`
- 年龄小于18并且 性别为男
    - `db.class0.find({age:{$lt:18},sex:'m'},{_id:0})`
        - 在 query 如果写多个条件默认即为 and 关系
   - `db.class0.find({$and:[{age:{$lt:18}},{sex:'m'}]},{_id:0})`

`$or`  逻辑或
- 年龄小于16或者年龄大于18
    - `db.class0.find({$or:[{age:{$lte:16}},{age:{$gt:18}}]},{_id:0})`

`$not`  逻辑非
- 查找年龄不小于18岁的
    - `db.class0.find({age:{$not:{$lt:18}}},{_id:0})`

`$nor`   not  (a or b)  ===> (not a) and (not b)
- 性别不是m且年龄不小于18
    - `db.class0.find({$nor:[{sex:'m'},{age:{$lt:18}}]},{_id:0})`

### 逻辑条件混合

- （年龄大于17 并且 为男生）  或者 姓名叫 Abby
    - `db.class0.find({$or:[{age:{$gt:17},sex:'m'},{name:'Abby'}]},{_id:0})`


- （年龄不大于18 或者为 女性） 并且 姓名 大于Lucy
    - `db.class0.find({$or:[{age:{$not:{$gt:18}}},{sex:'w'}],name:{$gt:'Lucy'}},{_id:0})`

## Array
`[1,2,3,4]`
* 数组是有序的数据集合
* mongo中数组也可以有多重数据元素混合

- 查找数组中包含某一条件的元素
    - 只要score数组中包含小于60的元素即可查询过滤
        - `db.class1.find({score:{$lt:60}},{_id:0})`

`$all`查找数组同时包含多项的文档
- 查找同时包含49  67的文档
    - `db.class1.find({score:{$all:[49,67]}},{_id:0})`

`$size`通过数组元素个数查找 
- 查找score中包含两个元素的文档
    -`db.class1.find({score:{$size:2}},{_id:0})`

`$slice`取数组的部分进行显示，在field中声明，显示数组中前两项
- `db.class2.find({},{_id:0,score:{$slice:2}})`
- 跳过第一项显示后面两项
    - `db.class2.find({},{_id:0,score:{$slice:[1,2]}})`

## 其他常用查找操作符

`$exists`通过某个域是否存在筛选（true表示存在false表示不存在）
- 查找不存在sex域的文档
    - `db.class1.find({sex:{$exists:false}},{_id:0})`

`$mod` 余数查找
- 找出年龄为单数的文档
    - `db.class1.find({age:{$mod:[2,1]}},{_id:0})`

`$type`找出指定数据类型的文档
- 查找name域值类型为2的文档
    - `db.class1.find({name:{$type:2}},{_id:0})`

## 查找结果的操作函数

`db.collection.distinct(filed)`查看某个域的值范围
- 获取某个域的值，去重
    - `db.class0.distinct('age')`

`pretty()`格式化显示查询结果
- `db.class0.find().pretty()`

`limit(n)`显示前n条结果
- 显示查询结果前三条
    - `db.class0.find({},{_id:0}).limit(3)`

`skip(n)`跳过前n条显示后面的查询结构
- 跳过前5条文档，显示后面的查询结果
    - `db.class0.find({},{_id:0}).skip(5)`

`count()`统计查询结果数量
- 在统计数量时要给出一定query条件
- 统计性别为w的文档个数
    - `db.class0.find({sex:'w'},{_id:0}).count()`

`sort({field: 1/-1})`
- 功能： 对查找结果排序
- 参数： 以键值对表示按照哪个field排序，1 表示升序，-1表示降序
- 查找结果按照降序排序
    - `db.class0.find({},{_id:0}).sort({age:-1})`
- 按照年龄升序排序，年龄相同时按照姓名降序
    - `db.class0.find({},{_id:0}).sort({age:1,name:-1})`

#### 函数的连续调用
`db.class0.find({},{_id:0}).sort({age:1}).limit(3)`

## 删除文档

`mysql ： delete from table where ... `  
`mongodb ： db.collection.remove(query,justOne)`

`remove(query,justOne)`
- 功能 ： 删除文档
- 参数 ： 
    - query  用法同find 
    - justOne 布尔值默认为false表示删除所有符合条件的文档，设置为true则表示只删除一条
- 删除所有不存在sex域的文档
    - `db.class1.remove({sex:{$exists:false}})`
- 删除第一条性别为w的文档
    - `db.class1.remove({sex:'w'},true)`

### 删除集合中所有文档
- 删除class1中所有文档
    - `db.class1.remove({})`

## 修改文档

`mysql ： update table set ... where ...`  
`mongodb: db.collection.update(query,update,upsert,multi)`

`update(query,update,upsert,multi)`
- 功能 ： 修改文档
- 参数 ： 
    - query  筛选条件用法同find
    - update  要修改成什么内容 通常配合修改操作符（修改器$set）使用
    - upsert  布尔值，默认是false，如果query没有筛选到文档则不做任何操作，如果设置为true 则如果query没有筛选到匹配文档则根据query和update内容插入新的文档
    - multi   布尔值 默认false 表示如果有多条符合条件文档则只修改第一条，如果设置为true则表示修改所有符合条件文档


- 将Tom的年龄修改为18
    - `db.class0.update({name:'Tom'},{$set:{age:18}})`
- 如果有name=Jame的文档则修改，如果没有则根据query update插入新的文档
    - `db.class0.update({name:'Jame'},{$set:{age:15}},true)`
- 修改所有年龄小于17的为18
    - `db.class0.update({age:{$lt:17}},{$set:{age:18}},false,true)`

    练习：

    1. 创建数据 名称 grade
       use  grade

    2. 创建集合 名称 class   

    3. 集合中插入若干（5-8条即可）文档 文档格式
    {name:'zhangsan',age:10,sex:'m',hobby:['a','b']}
     年龄范围 6-15
     爱好选择：draw  sing  dance  basketball  football  pingpong  computer 每个同学选择2-5项

       db.class.insert({name:'zhangsan',age:10,sex:'m',hobby:['draw','sing']})

    4. 查找练习
     查看班级所有学生信息
       find()

     查看班级中年龄为8岁的学生信息
       find({age:8})

     查看班级中年龄大于10岁学生信息
       find({age:{$gt:10}})

     查看班级中年龄在8-11岁之间的学生信息
       find({age:{$gte:8,$lte:11}})

     查看班级中年龄10岁且为男生的学生信息
       find({age:10,sex:'m'})

     查看班级中小于7岁或者大于14岁的学生
       find({$or:[{age:{$lt:7}},{age:{$gt:14}}]})

     查看班级中年龄为8岁或者11岁的学生
       find({age:{$in:[8,11]}})

     找到有2项兴趣爱好的学生
       find({hobby:{$size:2}})

     找到兴趣中 有draw的学生
       find({hobby:'draw'})

     找到既喜欢画画又喜欢跳舞的学生
       find({hobby:{$all:['draw','dance']}})

     统计兴趣有4项的学生人数
       find({hobby:{$size:4}}).count()

     找出本班年龄第二大的学生
       find().sort({age:-1}).skip(1).limit(1)

     查看本班学生兴趣爱好涵盖哪些方面
       db.class.distinct('hobby')

     找到年龄最大的三个学生
       find().sort({age:-1}).limit(3)

     删除所有年龄大于16或者小于7岁的学生除非他的爱好有三项以上
       remove({$or:[{age:{$gt:16}},{age:{$lt:7}}],{hobby:{$size:2}}})

## 修改操作符（修改器）

`$set`修改一个域的值
- Lily年龄修改为17 
    - `db.class0.update({name:'Lily'},{$set:{age:17}})`
- 为jame增加sex域
    - `db.class0.update({name:'Jame'},{$set:{sex:'m'}})`

`$unset`删除一个域
- 删除Abby 的sex域  sex后为空字符串
    - `db.class0.update({name:'Abby'},{$unset:{sex:''}})`

`$rename`修改域的名称
- 将sex域名改为gender
    - `db.class0.update({},{$rename:{sex:'gender'}},false,true)`

`$setOnInsert`如果使用update插入了文档，则将该修改器内容作为插入文档的一部分
- 如果插入了新文档则setOnInsert内容也会作为新文档一部分
    - `db.class0.update({name:'Jame'},{$set:{age:18},$setOnInsert:{gender:'m',tel:'123456'}},true)`

`$inc`加法修改器
- 所有人年龄加1 
    - `db.class0.update({},{$inc:{age:1}},false,true)`
    * 参数可以是正数负数 整数小数

`$mul`乘法修改器
- `db.class0.update({},{$mul:{age:0.5}},false,true)`
- 参数可以是正数负数 整数小数

`$min`如果筛选文档的指定域值小于min值则不修改，大于min值则修改为min值
- Levi age如果大于20则修改为20
    - `db.class0.update({name:'Levi'},{$min:{age:20}})`

`$max`如果筛选文档的指定域值大于max值则不修改，小于max值则修改为max值
- 如果Lenzer age 小于19则改为19
    - `db.class0.update({name:'Lenzer'},{$max:{age:19}})`

## 数组修改器

`$push`向数组中添加一项
- 给小红 score数组中添加一项91
    - `db.class1.update({name:'小红'},{$push:{score:91}})`

`$pushAll` 向数组中添加多项
- `db.class1.update({name:'小乔'},{$pushAll:{score:[94,10]}})`

`$pull``从数组中删除一项
- 从数组中删除一项
    - `db.class1.update({name:'小红'},{$pull:{score:78}})`

`$pullAll`
- 从数组中删除多项
    - `db.class1.update({name:'小乔'},{$pullAll:{score:[92,10]}})`

`$each`对多个值逐个进行操作
- 分别插入99  10
    - `db.class1.update({name:'小乔'},{$push:{score:{$each:[99,10]}}})`

`$position`指定插入位置
- 将67 插入到数组1号位置
    - `db.class1.update({name:'小明'},{$push:{score:{$each:[67],$position:1}}})`

`$sort`数组排序
- 将所有score域的数组降序排序
    - `db.class1.update({},{$push:{score:{$each:[],$sort:-1}}},false,true)`

`$pop`弹出一项 1表示弹出最后一项  -1弹出第一项
- 删除小明score中第一项
    - `db.class1.update({name:'小明'},{$pop:{score:-1}})`

`$addToSet`向数组中添加一项 但是不能添加重复的内容
- 如果数组中没有81 则添加81
    - `db.class1.update({name:'小刚'},{$addToSet:{score:81}})`

## 时间数据类型

>mongo中存储时间大多为 ISODate

- 存储当前时间方法
   1. new Date()  自动生成当前时间
       - `db.class2.insert({book:'Python入门',date:new Date()})`
   2. ISODate()  自动生成当前时间
       - db.class2.insert({book:'Python精通',date:ISODate()})
   3. Date()   将系统时间转换为字符串
       - db.class2.insert({book:'Python疯狂',date:Date()})


- `ISODate()`指定时间
    - 功能：生成mongo标准时间类型数据
    - 参数：如果不传参默认为当前时间
    - 传参表示指定时间
        - `“2018-01-01 12:12:12”`
        - `"20180101 12:12:12"`
        - `"20180101"`
   - `db.class2.insert({book:'Python崩溃',date:ISODate("2018-07-01 11:15:56")})`


- `valueOf()`时间戳
    - 获取当前标准时间时间戳
        - db.class2.insert({book:'Python涅槃',date:ISODate().valueOf()})

## Null 类型
1.  如果某个域存在却没有值可以赋值为null 
    - db.class2.insert({book:'Python死去活来',price:null})
2. 可以查找某个域不存在的情况
    - 如果date域不存在也能find到
    - db.class2.find({date:null})


## Object（内部文档）
- 文档内部某个域的值还是一个文档数据则这个文档就是内部文档类型数据通常使用外部文档域名 . 引用内部文档域名的方式使用内部文档
    - `db.class3.insert({name:"鲁迅", sex="m", book:{title:"狂人日记", price:48.8}})`
    - `db.class3.find({'book.title':'狂人日记'}) # 内部文档查找要加引号`
    - `db.class3.update({'book.title':'围城'},{$set:{'book.price':48.8}})`


- 通过数组下标直接操作某一项
    - 通过数组下标引用第一项进行查找
    - `db.class1.find({'score.0':{$gt:90}},{_id:0})`
    - `db.class1.update({name:'小刚'},{$set:{'score.1':80}})`

# 索引

>指建立指定键值及所在文档存储位置的对照清单，使用索引可以方便我们进行快速查找，减少遍历次数提高查找效率
>数据量较小时不适合创建索引，当数据库进行频繁的修改操作而不是查找操作时也不适合创建索引。针对一个集合并不是创建索引越多越好。

`ensureIndex()`
- 功能 ： 创建索引
- 参数 ： 索引域和索引选项
* 1表示正序索引 -1表示逆序索引
    - 根据name域创建索引
        - `db.class0.ensureIndex({name:1})`
        
        
- 查看集合中索引：`db.collection.getIndexes()`
- 自定义索引名称：`db.collection.ensureIndex({},{name:'myIndex'})`
    - `db.class0.ensureIndex({age:1},{name:'ageIndex'})`对age域创建索引命名ageIndex
- 删除索引：`db.collection.dropIndex("index")`
    - `db.class0.dropIndex({name：1})`
    - `db.class0.dropIndex('ageIndex')`
- 删除所有索引：`db.collection.dropIndexes()`
* _id是系统自动创建的主键索引，不能删除


## 索引类型
### 复合索引
- 根据多个域创建一个索引
    - `db.class0.ensureIndex({name:1,age:-1},{name:'name_age'})`

### 数组索引 ，子文档索引
- 如果对某个域的值为数组或者子文档的域创建索引，那么通过数组或者子文档中某一项进行查找也是索引查找
    - 如果对score创建了索引那么该查找就是索引查找
        - `db.class1.find({'score.1':88})`

### 唯一索引
- 创建索引的域要求值不能够重复
    - 对name创建唯一索引
        - `db.class0.ensureIndex({name:1},{unique:true})`
* 当对某个域创建了唯一索引就不能插入重复的值
  
### 稀疏索引（间隙索引）
- 只针对有指定索引域的文档创建索引，没有该域的文档不会插入到索引表
    - 只对有age域的文档创建索引
        - `db.class0.ensureIndex({age:1},{sparse:true})`
  
### 索引约束
* 索引表需要占用一定的数据库磁盘空间
* 当对数据进行增 删 改等写入操作时索引也需要更新，降低了数据修改的

# 聚合操作
>对文档的筛选结果进行整理统计
- `db.collection.aggregate()`
    - 功能 : 完成聚合操作
    - 参数 ： 聚合条件 ---》 聚合操作符

## 聚合操作符 

    $group 分组聚合，需要配合具体的分组统计选项

        $sum  : 求和
        db.class0.aggregate({$group:{_id:'$gender',num:{$sum:1}}})
        db.class0.aggregate({$group:{_id:'$gender',num:{$sum:'$age'}}})

        $avg : 求平均数
        db.class0.aggregate({$group:{_id:'$gender',avg:{$avg:'$age'}}})

        $max : 求最大值
        db.class0.aggregate({$group:{_id:'$gender',max:{$max:'$age'}}})

        $min  求最小值
        db.class0.aggregate({$group:{_id:'$gender',min:{$min:'$age'}}})

    $project 修改文档的显示效果，project值得用法和find函数field格式一致
        db.class0.aggregate({$project:{_id:0,name:1,age:1}})
        db.class0.aggregate({$project:{_id:0,Name:'$name',Age:'$age'}})

    $match 数据筛选，match值得用法同query一致
        过滤年龄大于18岁的数据文档
        db.class0.aggregate({$match:{age:{$gt:18}}})

    $limit  筛选前几条文档
        筛选前三条数据文档
        db.class0.aggregate({$limit:3})

    $skip 跳过几条文档显示
        跳过前三条文档
        db.class0.aggregate({$skip:3})

    $sort 将数据排序
        按照年龄排序
        db.class0.aggregate({$sort:{age:1}})

## 聚合管道 

- 聚合管道指的是将上一个聚合的操作结果给下一个聚合继续操作

        db.collection.aggregate([{聚合},{},{}...])

        e.g.  match --> project --> sort
        db.class0.aggregate([{$match:{gender:'m'}},{$project:{_id:0}},{$sort:{age:1}}])

        e.g.  group ---> match  找到重名学生
        db.class0.aggregate([{$group:{_id:'$name',num:{$sum:1}}},{$match:{num:{$gt:1}}}])



# 固定集合
- mongodb中可以创建大小固定的集合，称之为固定集合
- 特点：
    - 能够淘汰早期数据
    - 插入和顺序查找速度更快
    - 可以控制集合的空间大小
- 使用： 
    - 临时缓冲
    - 日志处理
    
`db.createColleciton(collection,{capped:true,size:10000,max:1000})`
- capped:true表示创建固定集合
- size：表示指定集合的大小、字节
- max：指定集合存放文档上限
    - 创建固定集合，size为1000  最多存3条文档
        - `db.createCollection('log',{capped:true,size:1000,max:3})`

# 文件存储

1. 存储文件路径    
`db.log.insert({filename:'test.mp4',size:247.8,path:"/home/tarena/mongodb/test.mp4"})`
- 优点 ： 
    - 节省数据库空间
    - 操作简单快捷
- 缺点 ： 
    - 当数据库或者文件位置发生变化时需要修改数据库内容

2. 存储文件本身
- 将文件以二进制的形式存储到数据库中
- 优点：数据库在文件就在，不会受到迁移等影响
- 缺点：占用数据库空间大，存取效率低

## GridFS存储大文件

- 大文件：在mongodb中认为 >16M 的文件为大文件
- GridFS方法：在mongodb中以两个集合配合的方法存储文件
    - fs.files：存储文件相关信息（文件名，文件类型）
    - fs.chunks：分块存储文件实际内容
    
    
- 存储文件：`mongofiles -d dbname  put  file`
    - dbname ： 要将文件存入的数据库，如果不存在自动创建
    - file ： 要保存的文件
        - 将test.mp4存入grid数据库
            - `mongofiles -d grid  put test.mp4`
- fs.files结构
    - `{ "_id" : ObjectId("5ba452a869d72e12d5cd4e46"), "chunkSize" : 261120, "uploadDate" : ISODate("2018-09-21T02:09:04.193Z"), "length" : 247759369, "md5" : "a94853f4f64b3e87bf98aea770855615", "filename" : "test.mp4" }`
- fs.chunks结构
    - `{ "_id" : ObjectId("5ba452a869d72e12d5cd4e59"), "files_id" : ObjectId("5ba452a869d72e12d5cd4e46"), "n" : 18, "data" : BinData(0,"G2.....qRv") }`
- 提取文件：`mongofiles -d dbname  get  file`
    - `mongofiles -d grid get test.mp4`



- 优点：操作方便，提供较好的存储命令，使用数据库存储文件方便移植
- 缺点：读写效率低


### 游标 cursor

- 通过获取操作数据库的返回结果，得到返回结果对象。
- 通过游标可以进一步获取操作结果数据。
- 将返回结果赋给一个js变量，作为查找结果游标
    - `var cursor = db.class0.find()`
- 查看是否有下一个结果
    - `cursor.hasNext()`
- 获取下一个结果
    - `cursor.next()`

# pymongo 模块

- 安装 ：  sudo pip3 install pymongo
- 操作步骤
    1. 创建mongodb的数据库连接对象
        - `conn = pymongo.MongoClient('localhost',27017)`
    2. 生成数据库对象 (\_\_setitem\_\_ \_\_getitem\_\_)
        - `db = conn.stu`
        - `db = conn['stu']`
    3. 生成集合对象
        - `myset = db.class0`
        - `myset = db['class0']`
    4. 集合操作 （增删改查索引聚合）
    5. 关禁数据库连接
        - conn.close()


```python
from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class1

# 数据操作
myset.insert({'name':'张铁林', 'King':"乾隆"})

# 关闭连接
conn.close()
```

### 插入操作
    insert()
    insert_many()
    insert_one()
    save()


```python
from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class1

# 数据操作
myset.insert([{'name':'张国立','King':'康熙'},\
    {'name':'陈道明','King':'康熙'}])
myset.insert_many([{'name':'唐国强','King':'雍正'},\
    {'name':'陈建斌','King':'雍正'}])
myset.insert_one({'name':'郑少秋','King':'乾隆'})
myset.save({'_id':1,'name':'聂远','King':'乾隆'})
myset.save({'_id':1,'name':'吴奇隆','King':'四爷'})

# 关闭连接
conn.close()
```

    /Users/haoen110/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:14: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
      
    /Users/haoen110/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:18: DeprecationWarning: save is deprecated. Use insert_one or replace_one instead
    /Users/haoen110/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:19: DeprecationWarning: save is deprecated. Use insert_one or replace_one instead


### 查找操作
- `find()`
    - 功能：查找数据库内容
    - 参数：同mongo shell find()
    - 返回值：返回一个结果**游标**
- `find_one()`
    - 功能：查询第一条符合条件的文档
    - 参数：同find（）
    - 返回值：返回一个**字典**
* 在pymongo中所有操作符的用法同mongo shell相同，只是操作时加引号，以字符串的方式写入python代码


- cursor对象的属性
    - next()
    - limit()
    - skip()
    - count()
    - sort()
    - pymongo -> sort([('age',1),('name',-1)])
    - mongo shell -> sort({age:1,name:-1})
* 使用for 或者next 使游标位置不再指向来头位置的时候调用limit  skip  sort就会报错


```python
from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class1

# 数据操作
cursor = myset.find({},{'_id':0})
print(cursor)

for i in cursor:
    print(i['name'],'---',i['King'])
    
dic = myset.find_one({},{'_id':0})
print(dic)
#---------------------------------------------

# 操作符使用
myset1 = db.class0 
cursor = myset1.find({'age':{'$lt':18}},{'_id':0})

for i in cursor:
    print(i)

# 获取下一条数据
# print(cursor.next())
# print(cursor.next())

# for i in  cursor.skip(1).limit(3):
#     print(i)

# for i in cursor.sort([('age',1),('name',-1)]):
#     print(i)

print('-'*10)
query = {'$or':[{'gender':'w'},{'age':{'$lt':19}}]}
cursor = myset1.find(query,{'_id':0})
for i in cursor:
    print(i)


# 关闭连接
conn.close()


```

    <pymongo.cursor.Cursor object at 0x10eac0b00>
    张铁林 --- 乾隆
    张铁林 --- 乾隆
    张铁林 --- 乾隆
    张国立 --- 康熙
    陈道明 --- 康熙
    唐国强 --- 雍正
    陈建斌 --- 雍正
    郑少秋 --- 乾隆
    吴奇隆 --- 四爷
    {'name': '张铁林', 'King': '乾隆'}
    {'name': 'James', 'age': 16.0, 'sex': 'm'}
    {'name': 'Howie', 'age': 16.0, 'sex': 'm'}
    {'name': 'Lenzer', 'age': 17.0, 'sex': 'm'}
    ----------
    {'name': 'Lucy', 'age': 18.0, 'sex': 'w'}
    {'name': 'James', 'age': 16.0, 'sex': 'm'}
    {'name': 'Howie', 'age': 16.0, 'sex': 'm'}
    {'name': 'Lenzer', 'age': 17.0, 'sex': 'm'}


### 修改操作
    update(query,update,upsert=False,multi=False)
    update_many()
    update_one()

### 删除操作
    remove(query,multi = True)
    multi默认是true表示删除所有query过滤文档
    设置为False表示只删除第一个

* python中：True == true 、 False  == false 、 None === null


```python
from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class0

# 数据操作
myset1.update({'name':'Jame'},{'$unset':{'tel':''}}, upsert=True)
myset1.update({'name':'Jame'},\
    {'$set':{'age':21}},multi = True)

#如果匹配文档不存在则插入
myset1.update({'name':'梁家辉'},\
    {'$set':{'King':'咸丰'}},upsert = True)

cursor = myset1.find({},{'_id':0})
for i in cursor:
    print(i)

# 关闭连接
conn.close()
```

    {'name': 'Lucy', 'age': 18.0, 'sex': 'w'}
    {'name': 'James', 'age': 16.0, 'sex': 'm'}
    {'name': 'Howie', 'age': 16.0, 'sex': 'm'}
    {'name': 'Lenzer', 'age': 17.0, 'sex': 'm'}
    {'name': 'Jame', 'age': 21}
    {'name': '阿辉', 'King': '咸丰'}
    {'name': '阿辉', 'King': '咸丰'}
    {'name': '梁家辉', 'King': '咸丰'}


    /Users/haoen110/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:13: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
      del sys.path[0]
    /Users/haoen110/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:15: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
      from ipykernel import kernelapp as app
    /Users/haoen110/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:19: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.


### 索引操作
    ensure_index()
    list_indexes()
    drop_index()
    drop_indexes()

### 聚合操作
    aggregate([])
    参数：和mongo shell一样
    返回值：返回和find()函数相同的游标对象


```python
from pymongo import MongoClient 

conn = MongoClient('localhost',27017)

db = conn.stu 

myset = db.class0 

#索引操作
#默认创建正向索引
# index = myset.ensure_index('name')
# print(index)

#创建逆向索引
# index = myset.ensure_index([('age',-1)])

#获取当前集合中索引
# for i in myset.list_indexes():
#     print(i)

#删除所有索引
# myset.drop_indexes()

#删除单个索引
# myset.drop_index("name_1")

#其他索引类型

#复合索引
# myset.ensure_index([('name',1),('age',-1)])

#唯一索引
# myset.ensure_index('name',\
#     name = "MyIndex",unique = True)

#稀疏索引
# myset.ensure_index('age',sparse = True)

#聚合操作
myset1 = db.class4 

p = [
     {'$group':{'_id':'$King','count':{'$sum':1}}},
     {'$match':{'count':{'$gt':1}}},
    ]

cursor = myset1.aggregate(p)

for i in cursor:
    print(i)

conn.close()
```

### 聚合练习

- grade数据库 class集合
1. 为所有人添加score域 值为
         {'chinese':88,'math':77,'english':78}

         from random import randint
         cursor = myset.find()
         for i in cursor:
            update({'_id':i['_id']},{'$set':{'score':{'chinese':randint(60,100),'math':randint(60,100),'english':randint(60,100)}}})


2. 按照性别分组统计每组人数

3. 统计每名男生的语文成绩

4. 将女生按照英语成绩降序排列

## pymongo 实现gridfs存储

    import  gridfs

    GridFS()
    功能： 生成grid数据库对象

    存储小文件
    import bson

    bson.binary.Binary()
    功能 ： 将bytes格式子串转换为mongodb的二进制存储格式
