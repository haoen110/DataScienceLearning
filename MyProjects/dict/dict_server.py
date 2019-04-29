"""
name: Enwei
data: 2019-04-29
email: haoenwei@outlook.com
"""

from socket import *
import os
import time
import signal
import pymysql
import sys
import getpass


# 定义需要的全局变量
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)


# 流程控制
def main():
    # 创建数据库连接
    db = pymysql.connect("localhost", "root", getpass.getpass("请输入root用户密码："), 'dict')

    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 忽略子进程信号
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit()
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c, db) # mysql自带锁，直接用父进程创建的db，不用担心冲突问题
            print("子进程准备处理请求")
            sys.exit()
        else:
            c.close()
            continue


def do_child(c, db):
    # 循环接受客户端请求
    while True:
        data = c.recv(1024).decode()
        if data == '1':
            do_register(c, db)
        if data == '2':
            name = do_login(c, db)
            if name:
                menu(c, db, name)
        if not data or data == '3':
            c.close()
            return


def do_register(c, db):

    cursor = db.cursor()
    username, passwd = c.recv(1024).decode().split()

    # 判断用户是否存在
    sql = "select * from user where name = '{}'".format(username)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r is not None:
        c.send("用户已存在！".encode())
        return

    # 用户不存在时插入用户
    sql = "insert into user (name, passwd) values('{}','{}')".format(username, passwd)
    cursor.execute(sql)

    try:
        db.commit()
        c.send('OK'.encode())
    except Exception as e:
        c.send(str(e).encode())
        db.rollback()
    else:
        print("注册成功！")


def do_login(c, db):

    # data = c.recv(1024).decode()
    #
    # if data == 'start':
    cursor = db.cursor()
    try:
        username, passwd = c.recv(1024).decode().split()
    except:
        c.send("e3".encode())
        return

    sql = "select * from user where name = '{}'".format(username)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r is None:
        c.send('e1'.encode())
        return
    else:
        sql = "select passwd from user where name = '{}'".format(username)
        cursor.execute(sql)
        r = cursor.fetchone()
        if r[0] == passwd:
            c.send("OK".encode())
            return username
        else:
            c.send("e2".encode())
        return
    # else:
    #     return


def menu(c, db, username):
    while True:
        data = c.recv(1024).decode()
        if data == '1':
            do_query(c, db, username)
        if data == '2':
            do_hist(c, db, username)
        if not data or data == '3':
            return


def do_query(c, db, username):

    cursor = db.cursor()

    def insert_hist():
        tm = time.ctime()
        sql = "insert into hist (name, word, time) values('{}','{}','{}')".format(username, word, tm)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

    while True:
        word = c.recv(1024).decode()
        if word == "##":
            break
        else:
            sql = "select interpret from words where word = '{}'".format(word)
            cursor.execute(sql)
            interpret = cursor.fetchone()
            if interpret is not None:
                c.send(interpret[0].encode())
                insert_hist()
            else:
                c.send("NO".encode())

    return


def do_hist(c, db, username):
    cursor = db.cursor()
    sql = "select * from hist where name = '{}'".format(username)
    cursor.execute(sql)
    r = cursor.fetchall()

    if not r:
        c.send("NO".encode())
        return
    else:
        c.send("OK".encode())

    for i in r:
        time.sleep(0.1)
        data = "{}    {}    {}".format(i[1], i[2], i[3])
        c.send(data.encode())

    time.sleep(0.1)
    c.send("##".encode())
    return


if __name__ == '__main__':
    main()
