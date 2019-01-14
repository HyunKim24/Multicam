# 유저(클라이언트)들이 웹페이지를 요청할 때 데이터를 보내고 싶다.
# Method 방식 => GET : 데이터를 헤더(header)에 싣고 전송
#                POST : 데이터는 바디(body)에 싣고 전송
# 요청(패킷) = 헤더 + 바디로 구성된다.
# 데이터 추출은 request 객체를 통해서 진행한다.
###############################################################
'''
GET의 예시 = 주소+?+데이터(키=값&키=값&...)
주소
https://m.news.naver.com/hotissue/main.nhn
물음표
?
데이터
sid1=102&cid=1080997&dummy=1901041331
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world3'

# ~/test?name=multi
# 이렇게 요청하면 데이터를 받아서 출력하는 라우트 처리
# 함수를 구성하시오
@app.route('/test')
def test():
    # get방식으로 데이터 획득하는 방법
    # request.args.get('키')
    name = request.args.get('name')
    print(name)
    return name

# 요청 주소
# http://127.0.0.1:5000/login?uid=가나다&upw=1234
# 화면에 아이디와 비번을 출력하는 해당 페이지를 구성하시오
@app.route('/login')
def login():
    uid = request.args.get('uid')
    # 이렇게도 데이터를 획득할 수 있으나 부재시 오류 발생
    # upw = request.args['upw']
    upw = request.args.get('upw')
    return uid + upw

if __name__=='__main__': # 이 코드를 메인으로 구동시 서버가동
    app.run(debug=True)
