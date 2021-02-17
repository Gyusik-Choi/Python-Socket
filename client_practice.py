import socket


HOST = '127.0.0.1'
# 서버에서 설정한 포트 번호
PORT = 8081

# 소켓 생성
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 연결
c.connect((HOST, PORT))

# 메세지 입력 받음
message = input()

# 서버로 메세지 전송
c.sendall(message.encode())

# 서버로부터 메세지 받음
message_from_server = c.recv(2048)

# 서버로부터 받은 메세지 출력
print("echo from server: " + message_from_server.decode())

# 참고
# 쉽게 배우는 데이터 통신과 컴퓨터 네트워크
# https://docs.python.org/ko/3/howto/sockets.html#history
# https://webnautes.tistory.com/1381
# https://nowonbun.tistory.com/668
# https://seolin.tistory.com/97