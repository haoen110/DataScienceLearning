# groupclient.py
from socket import *

#创建套接字
sockfd = socket()
sockfd.connect(('127.0.0.1',9999))
print(sockfd.recv(1024).decode())

name = input()
sockfd.send(name.encode())

data = sockfd.recv(1024)
print(">>",data.decode())

while True:
    #消息发送接收
    data = input("请输入：")
    if not data:
        break 
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print(">>",data.decode())

# #关闭套接字
sockfd.close()