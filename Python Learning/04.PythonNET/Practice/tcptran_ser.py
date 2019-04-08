# tcptran_ser.py
from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(('127.0.0.1', 9999))
sockfd.listen(5)

connfd, addr = (sockfd.accept())
print("Connected from", addr)


f = open('recv.jpeg', 'wb')

while True:
	data = connfd.recv(1024)
	if not data:
		break
	f.write(data)


f.close
connfd.send(b'Saving complete')
connfd.close()
sockfd.close()
