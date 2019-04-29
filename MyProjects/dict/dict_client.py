"""
name: Enwei
data: 2019-04-29
email: haoenwei@outlook.com
"""

from socket import *
import sys
import getpass


# 创建网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    try:
        s.connect((HOST, PORT))
    except Exception as e:
        print(e)
        return

    while True:
        print("""
        ==========Welcome============
         --- 1.注册 2.登录 3.退出 ---
        =============================
        """)
        try:
            cmd = int(input("请输入选项："))
        except Exception as e:
            print("命令错误")
            continue

        if cmd not in [1, 2, 3]:
            print("请输入正确选项")
            sys.stdin.flush() # 清除标准输入
            continue
        elif cmd == 1:
            do_register(s)
        elif cmd == 2:
            name = do_login(s)
            if name:
                menu(s)
        elif cmd == 3:
            s.send("3".encode())
            sys.exit("谢谢使用！")


def do_register(s):

    s.send('1'.encode())

    username = input("请输入用户名：")
    passwd = getpass.getpass("请输入密码，最多16位：")
    passwd1 = getpass.getpass("请重复输入密码：")

    if passwd != passwd1 or len(passwd) > 16:
        print("密码不符合要求！")
        return
    else:
        s.send((username+' '+passwd).encode())
        data = s.recv(1024).decode()
        if data == 'OK':
            print("注册成功！")
            return
        else:
            print("注册失败！", data)


def do_login(s):

    s.send('2'.encode())

    username = input("请输入用户名：")
    passwd = getpass.getpass("请输入密码：")
    # if not username or not passwd:
    #     print("用户名和密码不能为空！")
    #     s.send("end".encode())
    #     return

    # s.send("start".encode())
    s.send((username + ' ' + passwd).encode())

    data = s.recv(1024).decode()
    if data == 'OK':
        print("登录成功！")
        return username
    elif data == "e1":
        print("没有该用户名！")
        return
    elif data == "e2":
        print("密码错误！")
        return
    elif data == "e3":
        print("不合法的输入！")
        return


def menu(s):
    while True:
        print("""
        ==========Welcome============
         --- 1.查询 2.历史 3.退出 ---
        =============================
        """)
        try:
            cmd = int(input("请输入选项："))
        except Exception as e:
            print("命令错误")
            continue

        if cmd not in [1, 2, 3]:
            print("请输入正确选项")
            sys.stdin.flush() # 清除标准输入
            continue
        elif cmd == 1:
            s.send("1".encode())
            do_query(s)
        elif cmd == 2:
            s.send("2".encode())
            do_hist(s)
        elif cmd == 3:
            return


def do_query(s):
    while True:
        word = input("请输入要查询的单词，输入##退出：")
        if word == "##":
            s.send(word.encode())
            break
        s.send(word.encode())
        interpret = s.recv(1024).decode()
        if interpret != "NO":
            print(word, ":", interpret)
        else:
            print("没有查到该单词")
    return


def do_hist(s):
    data = s.recv(1024).decode()
    if data == "OK":
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                print("检索完成")
                break
            else:
                print(data)
    else:
        print("没有历史记录")
    return


if __name__ == '__main__':
    main()
