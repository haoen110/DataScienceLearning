from socket import * 
from time import sleep,ctime 

s = socket()
s.bind(('127.0.0.1',8888))
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
        print("Connect from",addr)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode())
        c.close()
s.close()