# jam_meeta

파이썬 장고를 이용한 간단한 잼라이브 웹애플리케이션입니다.
Channels를 이용하여 실시간으로 문제가 출제되도록 구현하였습니다.

git clone https://github.com/rimduhui/jam_meeta
pip install -r requirements.txt (pip가 안되시는 분들은 pip를 먼저 설치해주세요.)

127.0.0.1:8000 -> main 화면입니다. 문제를 제공하고 유저는 문제를 풉니다.
127.0.0.1:8000/login/ -> login 화면입니다. 이름을 입력하고 문제를 제공받습니다.
127.0.0.1:8000/leader/ -> leader 화면입니다. 다음문제, 초기화 기능을 합니다.

pycharm 가상환경에서 구현하였습니다.
