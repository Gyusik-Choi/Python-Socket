import socket

# 소켓 생성
# AF_INET: 인터넷 주소 체계 / SOCK_STREAM: 연결형 서비스(TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 생성한 소켓과 연결
# '': INADDR_ANY(시스템에 있는 모든 주소로 소켓에 연결할 수 있음)/ 8081: 포트번호 지정
s.bind(('', 8081))

# 클라이언트 대기
s.listen(2)

# 클라이언트 받음
c, address = s.accept()

while True:
    # 메세지 받음
    message = c.recv(2048)
    if not message:
        break
    # 메세지 출력
    print(message.decode())
    # 메세지 전송
    c.sendall(message)

s.close()

# 참고
# 쉽게 배우는 데이터 통신과 컴퓨터 네트워크
# https://docs.python.org/ko/3/howto/sockets.html#history
# https://webnautes.tistory.com/1381
# https://nowonbun.tistory.com/668
# https://seolin.tistory.com/97
