# f7의 발전 버전
# 실제 로그인은 로그인 페이지에서 아이디 비번을 넣고 
# 로그인을 눌렀을 때 작동한다
# 로그인화면을 만들어주는 html의 이해와 이를 처리하는 방법
# 을 알아야 한다.
# 웹 화면을 구성하는 요소
'''
(1~3번을 관장하는 기관 W3C)
1. HTML5 : 콘텐츠를 가지고 있다, 구조를 가지고 있다, 뼈대, 콘텐츠
2. CSS3  : 레이아웃담당, 프리젠테이션, 데코레이션, 디자인, 애니메이션 
3. JS    : 오퍼레이션 담당, 인터렉션(사용자와주고받기)
           이벤트 처리( 통신처리(ajax) 동적페이지(DHTML,DOM) 구성 )
           js를 중심으로 웹페이지를 만드는 기술
           앵귤러js(구글), ReactJS(페이스북), Vue(뷰에: 개발자커뮤니티)
           or
           JavaScript 프레임웤 => JQuery
'''
###############################################################
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # html의 태그들로 표현을 하면 브라우저는 파싱을 통해
    # 한줄 한줄 해석하여 화면을 그려나간다
    # 그러면서 <..> 태그로 구성된 부분은 화면에 그리지 않고
    # 해당 태그의 의미에 맞춰서 화면 처리를 한다.
    # <h2> : 헤드라인 태그 h1~h4
    return '<h1>hello world3</h1>'

@app.route('/login')
def login():
    # html파일을 찾아서 읽어서 텍스트를 리턴
    return render_template('login.html')

# 디비가 없는 관계로 
# 우리 회원은 아이디가 m, 비번 1 만 회원이다.
@app.route('/loginProc')
def loginProc():
    uid = request.args.get('uid')
    upw = request.args.get('upw')
    if uid == 'm' and upw == '1':
        # 회원이면 => [화면]:반값습니다. m님 -> 서비스
        # return '반갑습니다. %s님' %(uid) 
        # 요청에 대해 바로 응답하지 않고 다른 페이지로 요청을 던진다.
        # => 리다이렉트
        # 세션 생성 => 로그인 했음을 인지하는 방법, 사용자 정보 저장하는 용도
        return redirect('/main')
    else:
        # 회원 아니면 => [화면]:아이디나 비번을 확인해 주세요 -> 뒤로
        return '''
        <script>
            alert('아이디나 비번을 확인해 주세요');
            history.back();
        </script>
        '''
    # return uid+upw


# 메인 서비스 화면 ~/main
# 화면 내용은 그냥 서비스
@app.route('/main')
def main():
    # 로그인을 해야지만 진입할 수 있는 페이지이다.(원래)
    # 로그인 여부를 판단할수 있어야 거를 수 있다 => 세션
    return '서비스'

if __name__=='__main__': # 이 코드를 메인으로 구동시 서버가동
    app.run(debug=True)