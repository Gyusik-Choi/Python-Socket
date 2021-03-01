import socket
import threading


def send(client):
    while True:
        message = input()
        client.send(message.encode())


def receive(client):
    while True:
        message = client.recv(2048)
        print(client, message.decode())


HOST = '127.0.0.1'
PORT = 8081

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((HOST, PORT))

send_message = threading.Thread(target=send, args=(c, ))
receive_message = threading.Thread(target=receive, args=(c, ))

send_message.start()
receive_message.start()
