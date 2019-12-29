
# 服务器模型
- **硬件服务器**
    - 主机、集群
    - 厂商：IBM、HP、联想、浪潮
- **软件服务器**：编写的服务端应用程序，在硬件服务器上运行，一般依托于操作系统，给用户提供一套完整的服务
    - httpserver：处理http请求
    - webserver：网站的后端应用服务器程序
    - 邮箱服务器：邮件处理
    - ftp文件服务器：文件的上传下载


- 功能：网络连接、逻辑处理、数据交互、数据传输、协议的实现
- 结构：
    - c/s   客户端服务器模型
    - b/s   浏览器服务器模型


- 服务器**目标**：处理速度更快、并发量更高、安全性更强
    - 硬件要求：
        - 更高的配置
        - 更好的集成分布技术
        - 更好的网络优化
        - 网络安全技术
    - 软件要求：
        - 占用资源更少
        - 运行更稳定
        - 算法更优良
        - 安全性更好
        - 并发性更高
        - 更容易扩展

## 循环模型
- 循环接收客户端请求，处理请求。同一时刻只能处理一个请求，处理完毕后再处理下一个
    - 优点：实现简单，占用资源少
    - 缺点：无法同时处理多个客户端任务
    - 适用情况：处理的任务可以**短时间完成**，不需要建立并发，更适合udp使用
    
## 并发模型
- 能够同时处理多个客户端请求

### IO并发：IO多路复用（例如：select）
- 优点：资源消耗少，IO处理速度快
- 缺点：不能适用cpu密集型程序    
    
### 多进程/多线程并发
- 为每个客户端创建单独的进程线程，执行请求
- 优点：
    - 每个客户端可以长期占有服务器运行程序
    - 能够使用多核资源，可以处理IO或者cpu运算
- 缺点：消耗系统资源高

>#### 多进程并发模型--使用fork实现多进程并发（例如之后的ftp服务器）
1. 创建套接字，绑定，监听
2. 等待接收客户端请求
3. 创建新的进程处理客户端请求
4. 原有进程继续等待接收新的客户端连接
5. 如果客户端退出则关闭子进程

>*在父进程中忽略子进程状态改变，子进程退出自动由系统处理*  
>*`signal.signal(signal.SIGCHLD, signal.SIG_IGN)`*


```python
# fork_server.py
from socket import *
import os
import sys
import signal

# 客户端处理函数
def client_handler(c):
    print("处理子进程的请求：", c.getpeername())
    try:
       while True:
        data = c.recv(1024)
        if not data:
            break
        print(data)
        c.send("收到客户端的请求".encode())
    except (KeyboardInterrupt, SystemError):
        sys.exit()
    except Exception as e:
        print(e)
    c.close()
    sys.exit(0)

# 创建套接字
HOST = ""
PORT = 9999
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

print("进程%d等待客户端连接" % os.getpid())
# 在父进程中忽略子进程状态改变，子进程退出自动由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器推出")
    except Exception as e:
        print("Error:", e)
        continue
    
    # 为客户端创建新的进程，处理请求
    pid = os.fork()
    
    # 子进程处理请求
    if pid == 0:
        client_handler(c)
    # 父进程或者创建失败，都会继续等待下个客户端连接
    else:
        continue
```

    进程6254等待客户端连接
    处理子进程的请求： ('127.0.0.1', 63820)
    b'hello'
    处理子进程的请求： ('127.0.0.1', 63828)
    b'world'



    An exception has occurred, use %tb to see the full traceback.


    SystemExit: 服务器推出




    An exception has occurred, use %tb to see the full traceback.


    SystemExit: 服务器推出




    An exception has occurred, use %tb to see the full traceback.


    SystemExit: 服务器推出



    /Users/haoen110/miniconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3275: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
    /Users/haoen110/miniconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3275: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
    /Users/haoen110/miniconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3275: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)



```python
#tcp_client.py
from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr = ('127.0.0.1',9999)
sockfd.connect(server_addr)

while True:
    #消息发送接收
    data = input("发送>>")
    if not data:
        break 
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("接受到:",data.decode())

#关闭套接字
sockfd.close()
```

# ftp文件服务器

- 项目功能
    * **服务端**和**客户端**两部分，要求启动一个服务端，可以同时处理多个客户端请求
    * 功能
        1. 可以查看服务端文件库中所有的普通文件
        2. 从客户端可以下载文件库的文件到本地
	    3. 可以将本地文件上传的服务端文件库
	    4. 退出
        
**客户端使用print在终端打印简单的命令提示，通过命令提示发起请求**

>### 技术分析（fork、tcp并发）
- 每个功能要单独封装，整体功能写在一个类中
- 如何搭建整体架构，完成网络通讯

>### 功能分析
- 获取文件列表
   - 客户端：  
       - 发送请求
       - 得到回复判断能否获取列表
	   - 接收文件名称列表打印
   - 服务端： 
       * 接收请求
       * 判断请求类型
	   * 判断能否满足请求，回复信息确认
	   * 执行请求发送文件列表  
`os.listdir(path)`获取目录中文件列表  
`os.path.isfile()`判断是否为普通文件  
`os.path.isdir()`判断是否为目录  

>### 文件下载
- 客户端：
    * 发送请求 （文件名）
    * 得到回复判断能否下载
	* 下载文件
- 服务端：
    * 接收请求
    * 判断请求类型
	* 判断能否满足请求，回复信息确认
	* 执行请求发送文件


```python
'''
ftp 文件服务器
'''
from socket import *
import os 
import sys
import time
import signal  

#文件库路径
FILE_PATH = "~/Documents/ftpFile/"
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

#将文件服务器功能写在类中
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode()) 
            return 
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        files = ''
        for file in file_list:
            if file[0] != '.' and \
            os.path.isfile(FILE_PATH + file):
                files = files + file + '#'
        self.connfd.sendall(files.encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH + filename,'rb')
        except:
            self.connfd.send('文件不存在'.encode())
            return 
        self.connfd.send(b'OK')
        time.sleep(0.1)
        #发送文件
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        print("文件发送完毕")

    def do_put(self,filename):
        try:
            fd = open(FILE_PATH + filename,'wb')
        except:
            self.connfd.send('上传失败'.encode())
            return 
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        print("上传完毕")

#创建套接字,接收客户端连接,创建新的进程
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    #处理子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 8000...")

    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常:",e)
            continue 

        print("已连接客户端:",addr)
        #创建子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)
            #判断客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if not data  or data[0] == 'Q':
                    connfd.close()
                    sys.exit("客户端退出")
                elif data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == 'P':
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)

        else:
            connfd.close()
            continue


if __name__ == "__main__":
    main()
```


```python
'''
ftp 客户端
'''
from socket import * 
import sys 
import time 

#基本文件操作功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd 

    def do_list(self):
        self.sockfd.send(b'L') #发送请求
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完毕\n")
        else:
            #由服务器发送失败原因
            print(data)


    def do_get(self,filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完毕\n"%filename)
        else:
            print(data)

    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except:
            print("没有找到文件")
            return 

        self.sockfd.send(('P ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break 
                self.sockfd.send(data)
            f.close()
            print("%s 上传完成"%filename)
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')

#网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)  #文件服务器地址

    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except:
        print("连接服务器失败")
        return

    ftp = FtpClient(sockfd) #功能类对象
    while True:
        print("========== 命令选项 ===========")
        print(">>list")
        print(">>get file")
        print(">>put file")
        print(">>quit")
        print("===============================")

        cmd = input("请输入命令>>")

        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        elif cmd.strip() == "quit":
            ftp.do_quit()
            sockfd.close()
            sys.exit("谢谢使用")
        else:
            print("请输入正确命令!!!")
            continue

    
if __name__ == "__main__":
    main()
```

>#### threading的多线程并发
*对比多进程并发：*
    * 消耗资源较少
    * 线程应该更注意共享资源的操作
    * 在python中应该注意GIL问题，网络延迟较高，线程并发也是一种可行的办法
1. 创建套接字，绑定监听
2. 接收客户端请求，创建新的线程
3. 主线程继续接收其他客户端连接
4. 分支线程启动对应的函数处理客户端请求
5. 当客户端断开，则分支线程结束  
`import traceback`
`traceback.print_exc()`  
功能：更详细的打印异常信息


```python
from socket import * 
import os,sys 
from threading import *
import traceback 

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#客户端处理函数
def handler(connfd):
    print("Connect from",connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break 
        print(data.decode())
        connfd.send(b'Receive request')
    connfd.close()

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#等待客户端请求
while True:
    try:
        connfd,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception:
        traceback.print_exc()
        continue 

    t = Thread(target = handler,args = (connfd,))
    t.setDaemon(True)
    t.start()
```

# 集成模块的使用
python2：SocketServer  
python3：socketserver

- 功能：通过模块的不同类的组合完成**多进程/多线程**的tcp/udp的并发 

`StreamRequestHandler`处理tcp套接字请求  
`DatagramRequestHandler`处理udp套接字请求  

`TCPServer`创建tcp server  
`UDPServer`创建udp server  
  
`ForkingMixIn`创建多进程  
`ForkingTCPServer`-->  ForkingMinIn + TCPServer  
`ForkingUDPServer`-->  ForkingMinIn + UDPServer  
  
`ThreadingMixIn`创建多线程  
`ThreadingTCPServer`--> ThreadingMinIn + TCPServer  
`ThreadingUDPServer`--> ThreadingMinIn + UDPServer  


```python
# TCP
from socketserver import * 

#创建服务器类
# class Server(ForkingMixIn,TCPServer):
# class Server(ForkingTCPServer):
class Server(ThreadingMixIn,TCPServer):
    pass 

class Handler(StreamRequestHandler):
    def handle(self):
        #self.request ==> accept 返回的套接字
        print("Connect from",\
            self.request.getpeername()) 
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'Receive')


if __name__ == "__main__":
    server_addr = ('0.0.0.0',8888)

    #创建服务器对象
    server = Server(server_addr,Handler)
    #启动服务器
    server.serve_forever()
```


```python
# UDP
from socketserver import * 

#创建服务器类
class Server(ThreadingMixIn,UDPServer):
    pass 

class Handler(DatagramRequestHandler):
    def handle(self):
        while True: 
            data = self.rfile.readline()
            print(self.client_address)
            if not data:
                break 
            print(data.decode())
            self.wfile.write(b"Receive")

if __name__ == "__main__":
    server_addr = ('0.0.0.0',8888)

    #创建服务器对象
    server = Server(server_addr,Handler)
    #启动服务器
    server.serve_forever()
```

# HTTPServer  V2.0
- 作用
    1. 接收客户端请求
    2. 解析客户端请求
    3. 组织数据，形成HTTP response 
    4. 将数据发送给客户端
    

- 升级
    1. 采用多线程并发接收多个客户端请求
    2. 基本的请求解析，根据请求返回相应的内容
    3. 除了可以请求静态网页，也可以请求简单的数据
    4. 将功能封装在一个类中
    

- 技术点
    1. socket  tcp 套接字
    2. http协议的请求响应格式
    3. 线程并发的创建方法
    4. 类的基本使用


```python
#coding=utf-8
'''
http server v2.0
1.多线程并发
2.可以请求简单数据
3.能进行简单请求解析
4.结构使用类进行封装
'''
from socket import * 
from threading import Thread 
import sys
import traceback

#httpserver类 封装具体的服务器功能
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        #增添服务器对象属性
        self.server_address = server_addr
        self.static_dir = static_dir 
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)

    #设置监听等待客户端连接
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception:
                traceback.print_exc()
                continue
            #创建新的线程处理请求
            clientThread = Thread\
            (target = self.handleRequest,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    #客户端请求函数
    def handleRequest(self,connfd):
        #接收客户端请求
        request = connfd.recv(4096)
        #解析请求内容
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),":",requestHeaders[0])

        #获取具体请求内容
        getRequest = str(requestHeaders[0]).split(' ')[1]

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()

    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir + "/basic.html"
        else:
            filename = self.static_dir + getRequest
        try:
            f = open(filename)
        except Exception:
            #没有找到页面
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += '\r\n'
            responseBody = "Sorry,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self,connfd,getRequest):
        urls = ['/time','/tedu','/python']

        if getRequest in urls:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            if getRequest == "/time":
                import time
                responseBody = time.ctime()
            elif getRequest == '/tedu':
                responseBody = "Welcome to tedu"
            elif getRequest == '/python':
                responseBody = "人生苦短我用Python"
        else:
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += '\r\n'
            responseBody = "Sorry,not found the data"  

        response = responseHeaders + responseBody
        connfd.send(response.encode())

if __name__ == "__main__":
    #服务器IP
    server_addr = ('0.0.0.0',8000)
    #我的静态页面存储目录
    static_dir = './static'

    #生成对象
    httpd = HTTPServer(server_addr,static_dir)
    #启动服务器
    httpd.serve_forever()
```

# 协程基础

- 定义：纤程，微线程。协程的本质是一个单线程程序，所以协程不能够使用计算机多核资源。

- 作用：能够高效的完成并发任务，占用较少的资源。因此协程的并发量较高。

- 原理：通过记录应用层的**上下文栈区**，实现在运行中进行上下文跳转，达到可以选择性地运行想要运行的部分，以此提高程序的运行效率。

- 优点：
    - 消耗资源少
    - 无需切换开销
	- 无需同步互斥
	- IO并发性好

- 缺点：无法利用计算机多核


yield ---> 协程实现的基本关键字


### greenlet 
    - `greenlet.greenlet()`生成协程对象  
    - `gr.switch()`选择要执行的协程事件


```python
from greenlet import greenlet 

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch() # 会接着上一次的继续打印
    print(78)

#协程对象
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
```

    12
    56
    34
    78


### gevent
- 作用：
    - 将协程事件封装为函数
    - 生成协程对象  
    
`gevent.spawn(func,argv)`
- 功能：生成协程对象
- 参数： 
    - func  协程函数
    - argv  给协程函数传参
- 返回值：返回协程对象

`gevent.joinall()`  
- 功能：回收协程
- 参数：列表，将要回收的协程放入列表

`gevent.sleep(n)`  
- 功能：设置协程阻塞，让协程跳转
- 参数：n  阻塞时间
  
`from gevent import monkey`  
`monkey.patch_all()`  
- 功能：修改套接字的IO阻塞行为

* 必须在socket导入之前使用


```python
import gevent
from time import sleep 

def foo(a,b):
    print("a = %d,b = %d"%(a,b))
    gevent.sleep(2)
    print("Running foo again")

def bar():
    print("Running int bar")
    gevent.sleep(3)
    print("Running bar again")

#生成协程
f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)
# sleep(3)
print("===============")
gevent.joinall([f,g])
print("%%%%%%%%%%%%%%")
```

    ===============
    a = 1,b = 2
    Running int bar
    Running foo again
    Running bar again
    %%%%%%%%%%%%%%



```python
import gevent 

from gevent import monkey
monkey.patch_all()

from socket import * 
from time import ctime 

def server(port):
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',port))
    s.listen(3)
    while True:
        c,addr = s.accept()
        print("Connect from ",addr)
        # handler(c)  #循环服务器
        gevent.spawn(handler,c) #协程服务器

def handler(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(ctime().encode())
    c.close()

if __name__ == "__main__":
    server(8888)
```
