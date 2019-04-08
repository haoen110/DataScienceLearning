# groupserver.py
from select import select 
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 9999))
sockfd.listen(5)

# 连接客户端
connfd, addr = sockfd.accept()
print(addr, "连接成功")

# 发送用户名请求
tips = "请输入您在聊天室中要使用的用户名："
connfd.send(tips.encode())

# 接收用户名
name = connfd.recv(1024).decode()

# 发送进入聊天室提示
tips = name + "进入聊天室！"
connfd.send(tips.encode())

names = []
names.append(dict(addr = addr, name = name))

while True:
	data = connfd.recv(1024)
	connfd.send(data)
	
connfd.close()
sockfd.close()




