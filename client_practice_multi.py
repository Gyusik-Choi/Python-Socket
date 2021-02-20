import socket
import threading


HOST = '127.0.0.1'
PORT = 8081

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((HOST, PORT))

while True:
    message = input()
    if message == 'quit':
        break
    c.sendall(message.encode())
    message_from_server = c.recv(2048)
    print("message from server", message_from_server.decode())

c.close()
