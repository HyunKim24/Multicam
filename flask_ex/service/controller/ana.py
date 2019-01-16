# 주소 : ~/analaysis/...
# ~/analysis/init, ~/analysis/proc, ~/analysis/sum
# app라는 실제가 바뀌면(블루프린트로) 주소의 시작방식이 변경
from flask_ex.service.controller import bp_analysis as app

# ~/analaysis/init
@app.route('/init')
def init():
    return "분석 초기화면 홈"

# ~/analysis/proc
@app.route('/proc')
def proc():
    return "상세페이지 홈"

# ~/analysis/sum
@app.route('/sum')
def sum():
    return "합계 홈"