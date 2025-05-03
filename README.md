breif for what We did :


Client-Server Socket Communication Report
Objective:
The goal of this implementation is to establish a basic TCP/IP connection between a client and a server using Python's built-in socket module.
The server listens for incoming client connections, receives a message, and sends a response.
The client sends a message to the server and receives the acknowledgment.


server.py code :
-----------------------------------------------------------------------------------------------
import socket 

HOST = '192.168.1.6'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    communication_socket, address = server.accept()
    print("connected to {adress}")
    message = communication_socket.recv(1024).decode('utf-8')
    print("Message from client is; {message}")
    communication_socket.send("Got Your Message Thank You!".encode('utf-8'))
    communication_socket.close()
    print(f"connection with {address} ended!")
------------------------------------------------------------------------------------------------------

Functionality:
Creates a socket with AF_INET (IPv4) and SOCK_STREAM (TCP).

Binds to the given IP address and port.

Listens for incoming connections.

Accepts connections in a loop, receives a message from the client, sends a reply, and then closes the connection.



client.py code:
--------------------------------------------------------------------------
import socket

HOST = '192.168.1.6'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
-----------------------------------------------------------------------

Functionality:
Connects to the server at the specified IP and port.

Sends a message "Hello World!" to the server.

Receives and prints the response from the server.
    
