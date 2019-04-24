# tcptran_cli.py
from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)

server_addr = ('127.0.0.1', 9999)
sockfd.connect(server_addr)

f = open('send.jpeg', 'rb')

while True:
	data = f.read(1024)
	if not data:
		break
	sockfd.send(data)

data = sockfd.recv(1024)
print(data.decode())

f.close()
sockfd.close()
