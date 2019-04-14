from socket import * 

s = socket()

#设置端口立即释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#获取套接字选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

#获取套接字地址族类型
print(s.family)

#获取套接字类型
print(s.type)

s.bind(('192.168.207.129',8888))
#获取绑定地址
print(s.getsockname())

#获取套接字文件描述符
print(s.fileno())

s.listen(5)

while True:
    c,addr = s.accept()
    print("Connect from",c.getpeername())
    c.recv(1024)