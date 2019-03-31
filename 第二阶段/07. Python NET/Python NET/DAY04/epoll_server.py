from socket import * 
from select import *

#创建套接字作为我们关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建epoll对象
p = epoll()

#fileno ---> IO对象的字典
fdmap = {s.fileno():s}

#注册关注的IO
p.register(s,EPOLLIN | EPOLLERR)

while True:
    #进行IO监控
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注事件
            p.register(c,EPOLLIN | EPOLLHUP)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:    
            data = fdmap[fd].recv(1024)
            if not data:
                #客户端退出,从关注事件移除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')