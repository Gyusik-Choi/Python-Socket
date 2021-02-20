import socket
import threading


def connect_with_client(client, client_address):
    print("connect with ", client_address)
    try:
        while True:
            message = client.recv(2048)
            if message:
                print("received message from {}".format(client_address))
                print("message: {}".format(message.decode()))
            client.sendall(message)
    except:
        print("error of ", client)
    finally:
        client.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8081))
s.listen()

try:
    while True:
        c, address = s.accept()
        print(c, address)
        th = threading.Thread(target=connect_with_client, args=(c, address))
        th.start()
except:
    print("error")
finally:
    s.close()

# 참고
# https://nowonbun.tistory.com/668
# http://pythonstudy.xyz/python/article/24-%EC%93%B0%EB%A0%88%EB%93%9C-Thread
