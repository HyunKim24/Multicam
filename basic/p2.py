# 단일 데이터 > 수치형
# 변수 => 변하는 값, 값을 담는 그릇..
# 어떻게(변수명) => 알파벳, _, 숫자(두번째글자부터)
# 문장의 끝에는 ; 이런것 안쓴다.
# a가 1이란 값을 담고 있다? (x)
# a가 1이란 값을 가르키고(참조) 있다? (o)
# => 파이썬의 모든 요소는 객체다.
# 객체는 메모리상에 주소를 가진다.
# a는 1이란 객체를 가르킬 수 있는 주소값을 가진다.
a = 1
print(a)
a = 2
print(a)
a = "가나다"
print(a)
# 변수는 어떤 객체도 다 가르킬 수 있기 때문에,
# 사전에 정의된 함수명들도 사용이 가능하다. 해서 
# 중복되지 않게 조심히 사용한다.
b = 1.1
print(b)
a = 1
b = 2
print(a+b)
print(a,type(a))
###############################################
print(a - b)
print(a * b)
# 나눠지면 타입이 바뀜
print(a / b)
print(a % b)
# x의 y 제곱
print(2**3)
print(7/4)
# 나누고 소수점 이하는 버림
print(7//4)
# 많은 연산자가 있는데 우선순위는? 
# => ()를 사용하면 순위를 몰라도 적용 가능
print((1+2+3+4)*2)
# 실습
# a값은 90, b 값은 75, c값은 99이다. 평균값을 출력하시오
a = 90
b = 75
c = 99
print((a+b+c)/3)
###############################################
# 8 진수 : 0o12
# 10 진수 : 255
# 16 진수 : 0xFF => 0~9 A,B,C,D,E,F
a = 0xFF
print(a)

# 변수 <-> 상수(파이썬에서는 별도로 없다.)
# 상수 => 변하지 않는 값 = > 
# 편의상 개발자들은 변수명을 다 대문자로 사용
PI = 3.14
