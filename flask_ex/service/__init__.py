from flask import Flask, request, session, redirect, url_for
from flask_ex.service.model import initDBHelper, DBManager

def create_app(config_path='resource/config.cfg'):
    app = Flask(__name__)
    # 각종 설정 ...
    app.secret_key = 'fdgdfskgjshdlfh'
    # 1. 환경변수설정/사용
    initConfig(app,config_path)
    # 2. 디비설정
    initDBHelper(app)
    DBManager.init(app)
    DBManager.init_db()
    # 3. 에러설정 (404, 500, ... 각종 오류 코드 발생 시 일괄처리)
    initErrorPage(app)
    # 4. 라우트설정(블루프린트)
    initBlueprint(app)
    # 5. 라이프사이클처리 
    initReqRes(app)
    return app

def initErrorPage(app):
    from flask_ex.service.error import not_found
    app.register_error_handler(404,not_found)

def initConfig(app,config_path):
    # 1. 환경변수설정/사용: 프로그램에서 사용되는 고정된 정보(디비접속정보, 운용상필요한상수값)
    #    class로부터(객체), 리소스(파일), 운영체계로부터 가져올 수 있다.
    # 코드에 하드코딩 되어 있지 않고, 환경변수값을 읽어서 프로그램에 반영시키는 방식
    app.config.from_pyfile(config_path, silent=True )
    # class를 읽어서 객체로부터 환경변수를 획득한다. -> 
    # 직관성, 코드에 적용되어 있다
    # 내 위치가 하위에 있다 하더라도 from을 기술 할 때는 풀경로를 사용한다.
    from flask_ex.service.config import DBConfig
    app.config.from_object(DBConfig)

    # 로드된 환경 변수 값 확인
    # configCheck(app.config.items())
    # TEST_URL에 해당되는 값을 출력하시오
    # 환경 변수의 값은 그 의도대로 타입을 따라간다.
    print(app.config['DB_PORT'])
    # print(app.config.get('TEST_URL'))
    # print(type(app.config.get('SERVER_RUN_MODE_IS_REAL')))

def initBlueprint(app):
    # blueprint => 주제별로 페이지를 나눠서 개발이 가능 => controller
    # 회원관리:~/users/login, ~/users/logout, ~/users/signup
    from flask_ex.service.controller import bp_users, bp_analysis
    # 해당 모듈 덩어리채로 메모리에 올라온다 -> 객체가 만들어지듯이 사용에 관계없이
    from flask_ex.service.controller import user, ana 
    # 블루프린트를 flask 객체에 등록
    app.register_blueprint(bp_users,url_prefix = '/users')
    # 분석관리:~/analysis/init, ~/analysis/proc, ~/analysis/sum
    app.register_blueprint(bp_analysis,url_prefix = '/analysis')

def initReqRes(app):
    # (생애주기:브라우저에서 주소 치고 엔터 쳐서 화면에 보이기까지 사이클)
    # 어떤 페이지이든 하나의 통로를 거쳐서 개별 페이지로 가고
    # 응답도 동일하다. 이곳에 필터를 구현하여 요청을 걸러버린다.
    @app.before_first_request
    def before_first_request():
        print('서버가 가동하고 최초 요청시 단 한번 반응함 ')
    
    # 모든 요청이 들어오는 곳 => 세션 처리를 해야함
    @app.before_request
    def before_request(): pass
        # # 세션 검사를 해서 세션이 없으면 ~/users/login로 이동
        # if not 'user_id' in session: # 세션 없음
        #     # 요청 페이지가 /user/login이 아닌 경우에만 포워딩
        #     if request.url.find(url_for('users_bp.login')) < 0:
        #         # return redirect('/users/login')
        #         # url_for(blueprint명.함수명)
        #         return redirect(url_for('users_bp.login'))
        # else:
        #     # 있으면 아무것도 안한다.
        #     print('모든 요청이 가장 먼저 들어오는 곳',request.url)

    # 모든 응답이 지나가는 곳, 공통 작업이 있을 경우 처리
    @app.after_request
    def after_request(res):
        print('매 요청이 처리되고 나서 응답이 지나가는 곳')
        return res
    
    @app.teardown_request
    def teardown_request(exception):
        print('브라우저가 응답하고 나서 실행')
        return '브라우저가 응답하고 나서 실행'

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        print('http 요청(app컨텍스트) 완전히 종료되고 호출')

def configCheck(items):
    # print(items)
    # 환경 변수 키, 환경 변수 값 출력
    for key, value in items:
        print(key,value)







