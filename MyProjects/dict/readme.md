# 项目分析
- 服务器：登录、注册、查词、历史记录
- 客户端：打印界面、发出请求、接收反馈、打印结果
- 技术点：
    - 并发：sys.fork
    - 套接字：tcp 套接字
	- 数据库：mysql
	- 查词：文本
- 工作流程：创建数据库，存储数据，搭建通信框架，建立并发关系，实现具体功能封装

1. 创建数据库存储数据

       dict
       user ： id  name   passwd
       hist :  id  name   word   time
       words : id  word   interpret
       create database dict default charset=utf8;
       create table user (id int primary key auto_increment,name varchar(32) not null,passwd varchar(16) default '000000');
       create table hist(id int auto_increment primary key,name varchar(32) not null,word varchar(32) not null,time varchar(64));
       create table words (id int auto_increment primary key,word varchar(32) not null,interpret text not null);

2. 搭建基本框架
- 服务器  
    - 创建套接字
    - 创建父子进程
        - 子进程：等待处理客户单端请求
        - 父进程：继续接收下一个客户端连接
- 客户端 
    - 创建套接字
    - 发起连接请求
    - 一级界面（登录，注册，退出）
        - 登录成功
            - 二级界面（查词，历史记录）

3. 功能实现
- 注册   
    - 客户端
        1. 输入注册信息
	    2. 将注册信息发送给服务器
	    3. 得到服务器反馈
    - 服务端
        1. 接收请求
	    2. 判断是否允许注册
	    3. 将结果反馈给客户端
	    4. 注册信息插入数据库

>cookie  
>import  getpass  
>passwd = getpass.getpass()  
>功能：隐藏密码输入