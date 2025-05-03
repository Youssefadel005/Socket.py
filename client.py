import socket

HOST = '192.168.1.6'
PORT=9090
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((HOST,PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))



