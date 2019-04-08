
# IO
    IO   input   output
    在内存中存在数据交换的操作都可以认为是IO操作
    和终端交互 ： input   print
    和磁盘交互 ： read  write
    和网络交互 ： recv   send

- IO密集型程序：在程序执行过程中存在大量IO操作，而cpu运算操作较少，消耗cpu较少，运行效率较低

- 计算密集型程序（CUP密集型程序）：在程序执行中CPU运算较多，IO操作相对较少，消耗CPU大，运行速度快

- IO分类
    - 阻塞IO   
    - 非阻塞IO   
    - IO多路复用

## 阻塞IO  
- 阻塞IO是IO的默认形态，是效率较低的一种IO情形。
- 阻塞情况
    - 因为某种条件没有达成造成的阻塞
        - e.g.  accept   input   recv
    - 处理IO数据传输时间较长形成的阻塞
        - e.g.  网络传输过程，文件读写过程

## 非阻塞IO 
- 通过修改IO事件的属性，使其变为非阻塞状态（让一些条件阻塞函数不再阻塞）
    - 非阻塞IO往往和循环判断一起使用
            s.setblocking(False)  
            将套接字设置为非阻塞状态


```python
# 设置非阻塞
from socket import * 
from time import sleep,ctime 

s = socket()
s.bind(('127.0.0.1',9999))
s.listen(3)

#将套接字设置为非阻塞
s.setblocking(False)

while True:
    print("Waiting for connect...")
    try:
        c,addr = s.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue 
    else:
        print("Connected from",addr)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode())
        c.close()
s.close()
```

- 超时检测
    - 将原本阻塞的函数设置一个最长阻塞时间，如果时间内条件达成则正常运行，如果仍然阻塞则视为超时，继续向下运行或产生异常

            s.settimeout(sec)  
            设置套接字的超时时间


```python
# 设置超时时间
from socket import * 
from time import sleep,ctime 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

#将套接字设置超时时间
s.settimeout(5)

while True:
    print("Waiting for connect...")
    try:
        c,addr = s.accept()
    except timeout:
        print(ctime())
        continue 
    else:
        print("Connect from",addr)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode())
        c.close()
s.close()
```

# IO多路复用
- 定义：同时监控多个IO事件，当哪个IO事件准备就绪就执行哪个IO事件，以此形成可用同时操作多个IO的并发行为，避免一个IO阻塞，造成所有IO都无法执行。
- **IO准备就绪**：是一种IO必然要发生的临界状态


- IO多路复用的编程实现
    1. 将IO设置为关注IO
    2. 将关注IO提交给内核监测
    3. 处理内核给我们反馈的准备就绪的IO
    
    
- 具体方案： 
        select --> linux   unix  windows  
        poll   --> linux   unix
        epoll  --> linux   unix    

# select
`import select`  
`rs,ws,xs = select(rlist, wlist, xlist[, timeout])`
- 功能：监控IO事件，阻塞等待IO事件发生
- 参数：
    - rlist..列表..存放我们监控**等待处理**的IO事件
    - wlist..列表..存放我们要**主动操作**的IO事件
    - xlist..列表..我们要关注**出错处理**的IO事件
    - timeout..超时时间
- 返回值：
    - rs..列表..rlist中准备就绪的IO
    - ws..列表..wlist中准备就绪的IO
	- xs..列表..xlist中准备就绪的IO

- 注意：
    1. wlist中如果有IO事件则select立即回返回为ws
    2. 在处理IO过程中不要处理一个客户端长期占有服务端使服务端无法运行到select的情况
	3. IO多路复用占用计算机资源少，io效率高


```python
from select import select 
from socket import *

#创建套接字作为我们关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9999))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    #提交监测我们关注的IO等待IO发生
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) #添加到关注列表
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                # r.send(b'Receive your message')
                #将客户端套接字放入wlist列表
                wlist.append(r)
                
    for w in ws:
        w.send(b'Receive your message')
        wlist.remove(w)

    for x in xs:
        if x is s:
            s.close()
```

# 位运算

- 整数按照二进制位进行运算
    - &：按位与
    - |：按位或
    - ^：按位异或
    - <<：左移
    - \>>：右移

        11    1011

        14    1110

        14 & 11 ： 1010    一0则0

        14 | 11 ： 1111    一1则1

        14 ^ 11 ： 0101    相同为0不同为1

        11 << 2 ： 101100  右侧补零
        14 >> 2 ： 11

# poll
1. 创建poll对象
        p = select.poll()
2. 添加注册事件
        p.register(s, POLLIN | POLLERR)

        POLLIN   POLLOUT  POLLERR  POLLHUP  POLLNVAL
        rlist    wlist    xlist    断开     无效数据

        p.unregister(s) 从关注事件中移除

3. 阻塞等待IO发生
        events = p.poll()
    - 功能：阻塞等待IO发生
    - 返回值：events 是一个列表，列表中给每一个元素都是一个元组，代表一个发生的IO事件
        
            [(fileno, event),(),()....]
            就绪IO的文件描述符， 具体就绪事件

    - 需要通过文件描述符（fileno）找到对应的IO对象
          {s.fileno() : s}

4. 处理具体的IO


```python
from socket import * 
from select import *

#创建套接字作为我们关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9999))
s.listen(5)

#创建poll对象
p = poll()

#fileno ---> IO对象的字典
fdmap = {s.fileno():s}

#注册关注的IO
p.register(s,POLLIN | POLLERR)

while True:
    #进行IO监控
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注事件
            p.register(c,POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLIN:    # 若是真，POLLIN就绪
            data = fdmap[fd].recv(1024)
            if not data:
                #客户端退出,从关注事件移除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')
```

# epoll
- 使用方法：基本与poll方法相同
    -  将生产对象 poll() 改为epoll()
    -  将所有poll对象事件改为epoll对象事件

- 区别 ：
    - epoll 的效率要比 poll和select 高
    - epoll 的事件触发方式更多


```python
from socket import * 
from select import *

#创建套接字作为我们关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9999))
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
```
