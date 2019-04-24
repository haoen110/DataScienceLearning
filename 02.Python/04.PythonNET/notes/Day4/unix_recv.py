from socket import *
import os

#确定套接字文件
sock_file = './sock_file'

#判断文件是否已经存在
if os.path.exists(sock_file):
    os.remove(sock_file)

#创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定套接字文件
sockfd.bind(sock_file)

#监听
sockfd.listen(3)

#消息收发
while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if data:
            print(data.decode())
            c.send(b"Receive")
        else:
            break 
    c.close()
sockfd.close()
