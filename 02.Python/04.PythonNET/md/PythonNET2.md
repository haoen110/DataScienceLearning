
# UDP应用：广播
- 广播：一点发送，多点接收
- 广播地址：一个网段内有一个指定的广播地址，是该网段的最大地址
    - 192.168.2.255
- 广播风暴：一个网络中有大量的广播就会产生广播风暴占用大量带宽，影响正常的访问速度


```python
# 接受广播：
from socket import * 

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)

#设置套接字可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#固定接收端口
s.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("从{}获取信息:{}".\
            format(addr,msg.decode()))
    except (KeyboardInterrupt,SyntaxError):
        raise 
    except Exception as e:
        print(e)
s.close()
```


```python
# 发送广播
from socket import *
from time import sleep 

#设置目标地址
dest = ('192.168.2.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

#设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("来呀,带你去看晴空万里".encode(),dest)

s.close()
```

# TCP应：http传输

- http协议：超文本传输协议，是一个应用层协议
- 用途：网页数据的传输，数据传输方法

- 特点 ： 
    1. 应用层协议，传输层使用tcp服务
    2. 简单，灵活，多种语言都有http相关操作接口
    3. 无状态的协议，即不记录用户传输的信息
    4. http1.1  支持持久连接


1. *一端通过http请求的格式发送具体请求内容，另一端接收http请求，按照协议格式解析*


2. *获取真实请求后按照http协议响应格式组织回复内容，回发给请求方，完成一次数据交互*

## http请求（request）

- 请求行：具体的请求类别和请求内容
    - 格式：GET / HTTP/1.1（请求类别 请求内容 协议版本）
    - 请求类别：表示请求的种类
        - GET      获取网络资源
        - POST     提交一定的附加信息，得到返回结果
        - HEAD     获取响应头
        - PUT      更新服务器资源
        - DELETE   删除服务器资源
        - CONNECT  
        - TRACE    用于测试
        - OPTIONS  获取服务器性能信息

- 请求头：对请求内容的具体描述信息
    - Accept-Encoding: gzip, deflate
    - Accept-Language: zh-CN,zh;q=0.9
    - Cache-Control: max-age=0
    - Connection: keep-alive

- 空行

- 请求体：请求参数或者是提交内容


## http响应（response）

- 响应行：反馈响应的情况
    - 格式 ： HTTP/1.1 200 OK（协议版本 响应码 附加信息）
    - 响应码：响应的具体情况
        - 1xx ： 提示信息，表示请求成功
	    - 2xx ： 响应成功
	    - 3xx ： 响应需要重定向
	    - 4xx ： 客户端错误
	    - 5xx ： 服务端错误
    - 常见响应码：
        - 200  成功
        - 404  请求内容不存在
		- 401  没有访问权限
		- 500  服务器发生未知错误
		- 503  暂时无法执行

- 响应头：对响应内容的具体描述
    - Connection: keep-alive
    - Content-Encoding: gzip
    - Content-Type: text/html
    - Date: Thu, 06 Sep 2018 09:11:18 GMT

- 空行

- 响应体：返回给请求端的具体内容


```python
from socket import * 

#创建tcp套接字
s = socket()

s.bind(('0.0.0.0',8000))
s.listen(5)

while True:
    c,addr = s.accept()
    print("Connect from",addr)
    data = c.recv(4096)
    print("*******************")
    print(data) #浏览器发来的http请求
    print("*******************")

    #组织响应内容
    data = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>Welcome back Home</h1>
    <p>这是一个测试</p>
    '''
    c.send(data.encode())
    c.close()

s.close()
```

# 要求
>    
1. 什么是http协议
2. 请求的格式和每一部分的功能
3. 响应的格式和每一部分功能
4. 常见的请求类型和响应码代表什么

通过tcp套接字完成一个文件的发送，将一个文件从客户端发送给服务端，或者从服务端发送给客户端均可，文件可以是文本，也可以是图片

# HTTPServer


```python
# 编写简易的HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>主页</title>
</head>
<body>
    <h1>My first html page</h1>
</body>
</html>
```


```python
# 编写本地服务端
from socket import * 

def handleClient(connfd):
    connfd.recv(4096)
    # request = connfd.recv(4096)
    # #将request请求按行分割打印出来显示
    # request_lines = request.splitlines()
    # for line in request_lines:
    #     print(line.decode())

    try:
        f = open("basic.html")
    except IOError:
        response = "HTTP/1.1 404  not found\r\n"
        response += "\r\n"  #空行
        response += "====Sorry not found====="
    else:
        response = "HTTP/1.1 200  OK\r\n"
        response += "\r\n"  #空行
        response += f.read()
    finally:
        #发送给浏览器
        connfd.send(response.encode())

#创建套接字
def main():
    sockfd = socket()

    # 设置端口重用
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 绑定监听
    sockfd.bind(('0.0.0.0',9999))
    sockfd.listen(3)
    print("Listen to the port 9999")

    while True:
        connfd,addr = sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()

if __name__ == "__main__":
    main()
```

在浏览器中运行127.0.0.1:9999
