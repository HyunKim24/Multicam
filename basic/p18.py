############################################################## 
# s/w는 죽으면 안된다!
# 죽을 수 있는 그런 정황이나 의심스러운 부분
# 사용자 입력을 받아서 처리되는 부분(통제가 안되는 부분)
# I/O를 처리하는 부분(파일, 네트워크 등등)
# 이런 부분에 대한 해결방안 =>
# 예외처리
##############################################################
# Exception: 모든 예외상황의 수퍼클래스
# 예외상황이 뭐가 될지 모르겠다. => Exception => 일단 해결됨 
try: # 일반 수행문(의심이 되는 부분)
    print(1)
    a = 1/0
    # a = 1/0
    print(2)
except Exception as e: # 예외가 발생하면
    print(3,e)
else: # 예외가 발생 안하면
    print(4)
finally: # 무조건 마무리 수행코드
    print(5)