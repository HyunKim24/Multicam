# 함수화 처리
# 아이디, 비번을 인자로 입력 받아서, 재활용성을 높이고, 모듈화의 모양새를 갖춘다.
    import pymysql as my

def login_sql(uid,upw):
    connection = None
    row = None # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='12341234', # 디비 접속 비번
                                db='python_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정

        if connection:
            print('디비 오픈')
            ##################################################################
            with connection.cursor() as cursor: 
                # 파라미터 자리를 '' 포함해서 %s로 대체
                # 'm' => %s
                # 방법 1
                sql = "select * from users where uid=%s and upw=%s;"
                cursor.execute(sql,(uid,upw))
                
                # 방법 2 : 적절히 섞어서 사용한다.(적합한 타이밍이 나온다)
                # select * from users where uid=m and upw=1;
                # sql = "select * from users where uid='%s' and upw='%s';" %('m','1')
                # print(sql)
                # cursor.execute(sql)
                
                row = cursor.fetchone()
                # {'id': 1, 'uid': 'm', 'upw': '1', 'name': '멀티', 'regdate': datetime.datetime(2019, 1, 7, 14, 16, 4)}
                print(row)
                print("%s님 반갑습니다." %row['name'])
                # cursor.close()
            ##################################################################
    except Exception as e:
        print('->',e)
        row =None
    finally:
        if connection:
            connection.close()
            print('디비 닫기') 
    return row 

# 주식 종목 리스트 가져오기(코드기준 정렬)
def selectTradeData():
    connection = None
    rows = None # 주식정보들을 담는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='12341234', # 디비 접속 비번
                                db='python_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 퀴리 수행
        with connection.cursor() as cursor: 
            sql = '''
                select 
                    code, name, cur, high, low 
                from 
                    tbl_trade
                order by code asc
                limit 0,10;
            '''
            cursor.execute(sql)    
            # 여러개 데이터를 다 가져올때        
            rows = cursor.fetchall()
    except Exception as e:
        print('->',e)
        rows =None
    finally:
        if connection:
            connection.close()
    return rows 

# 키워드를 이용하여 이름에 해당 키워드가 포함된 주식 목록을 리턴한다.
def selectStockByKeyword(keyword):
    connection = None
    rows = None # 해당 정보들을 가져오는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='12341234', # 디비 접속 비번
                                db='python_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 퀴리 수행
        with connection.cursor() as cursor: 
            sql = '''
                select 
                    code, cur, high, low, name
                from 
                    tbl_trade 
                where name like '%%%s%%';
            '''% keyword
            cursor.execute(sql)    
            # 여러개 데이터를 다 가져올때        
            rows = cursor.fetchall()
    except Exception as e:
        print('->',e)
        rows =None
    finally:
        if connection:
            connection.close()
    return rows


# code를 이용하여 해당 종목 정보를 모두 가져온다.
def selectOneStockInfo(code):
    connection = None
    row = None # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='12341234', # 디비 접속 비번
                                db='python_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정
        with connection.cursor() as cursor: 
            sql = "select * from tbl_trade where code = %s;"
            cursor.execute(sql,(code,))
            row = cursor.fetchone()
    except Exception as e:
        print('->',e)
        row =None
    finally:
        if connection:
            connection.close()
    return row

# 수정하기 : 코드를 이용하여 cur, rate를 변경한다
# 변경의 성공 여부는 영향을 받은 row의 수가 1이상일 경우 해당된다. => 리턴값
# stock : 타입이 dict, 키는 컬럼명을 따라간다
def updateStockInfo(stock):
    connection = None
    result = None # 수정 결과
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='12341234', # 디비 접속 비번
                                db='python_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정
        with connection.cursor() as cursor: 
            sql = '''
                update tbl_trade 
                set cur=%s, rate=%s 
                where code=%s;
              '''
            cursor.execute(sql,(stock['cur'],stock['rate'],stock['code']))
        # 커밋 수행 => 실제 디비에 반영시켜라
        # update, delete, insert 다 해당됨
        connection.commit()
        # 영향을 받은 로우의 수를 반환해라
        result = connection.affected_rows()
    except Exception as e:
        print('->',e)
        result = 0
    finally:
        if connection:
            connection.close()
    return result


# 삭제하기
def deleteStockInfo(code):
    connection = None
    result = None # 수정 결과
    try:
        connection = my.connect(host='localhost', # 디비 주소
                                user='root',      # 디비 접속 계정
                                password='12341234', # 디비 접속 비번
                                db='python_db',      # 데이터베이스 이름
                                #  port=3306,         # 포트
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # 커서타입지정
        with connection.cursor() as cursor: 
            sql = '''
                delete from tbl_trade where code=%s;
              '''
            cursor.execute(sql,code)
        connection.commit()
        result = connection.affected_rows()

    except Exception as e:
        print('->',e)
        result = 0
    finally:
        if connection:
            connection.close()
    return result


# 테스트 코드-> 이코드를 직접 구동할때만 작동되어야 한다
if __name__ =='__main__':
    # print('=>',login_sql('m','1'))
    # rows = selectTradeData()
    # if rows:print(rows)
    # else: print('데이터가 없다')
    # print('='*100)
    # print(selectOneStockInfo('000020'))
    # for a in selectOneStockInfo('000020'):
    #     print(a,b)
    # dic = {
    #     'cur':'3',
    #     'rate':'3.1',
    #     'code':'012330'
    # }
    # print("성공" if updateStockInfo(dic) else "실패")
    print( deleteStockInfo('000030') )
    