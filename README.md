# Python-Socket

네트워크를 공부하면서 socket을 통한 서버와 클라이언트 채팅 프로그램을 Python으로 구현해보았다.

현재는 메시지를 한번만 보내면 연결이 종료된다.

더 발전시키고 싶은 부분은 연결을 계속 유지 시키는 것과 다수의 클라이언트를 받을 수 있도록 하는 것이다.



메세지를 계속 보낼 수 있도록 수정됐다.

연결을 유지 시킬 수 있고, 다수의 클라이언트가 접속할 수 있도록 수정됐다.

더 발전시키고 싶은 부부은 만약에 채팅방처럼 구성하다고 했을 때 각자의 채팅방을 어떻게 구분하고 어떻게 다같이 메세지를 공유할 수 있을지다.



다같이 메세지를 공유할 수 있도록 수정했다. 배열에 접속하는 클라이언트들을 담고 for 문을 이용해서 본인을 제외하고 다른 클라이언트들에게 서버에서 메세지를 보내도록 했다.

클라이언트는 메세지 수신과 전송을 하는 쓰레드를 따로 구분했다.

채팅방을 구현한다고 하면 방을 어떻게 구분할 수 있을지 추가 학습이 필요하다.

