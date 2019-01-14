'''
step 1
"게임의 제목을 입력하세요" 프럼프트 출력
"적당한 제목(영문)" 입력하면 다음 단계 진행
'''
'''
step 1-1 게임 제목은 28자이내로 입력받는다
입력하지 않으면 "게임 제목이 입력되지 않았습니다. 다시 입력하세요"
넘으면 "게임 제목이 28자를 초과합니다 다시 입력하세요"
28자 이내면 ok
'''
while True:
    game_title = input("게임의 제목을 28자이내로 입력하세요\n")
    if len(game_title) == 0:
        print('게임 제목이 입력되지 않았습니다. 다시 입력하세요')
    elif len(game_title) > 28:
            print('게임 제목이 28자를 초과합니다 다시 입력하세요')
    else:
        break


'''
step 2 =는 한줄에 30개 글자는 총 몇개 가능? 28자가능
===========================
=     게임제목(중앙정렬)   = 
=     v 1.0.0             =
===========================
이렇게 출력
'''
TITLE_LEN = 30
print( '='*TITLE_LEN)
txt = '={0:^%s}=' %(TITLE_LEN-2)
print(txt.format(game_title))
print(txt.format('v 1.0.0'))
print( '='*TITLE_LEN)


'''
step 3
게이머의 이름을 입력하세요?
-> 이름을 넣지 않으면 "뭐라뭐라 하고" 다시 입력
'''
while True:
    gammer = input('게이머의 이름을 입력하세요?\n')
    if not gammer:
        print('이름을 입력하지 않았습니다.')
    else:
        break

'''
step 4
AI의 숫자를 입력하세요?
-> 숫자를 안넣으면 "경고 메세지" 다시 입력
-> 숫자가 아닌 값을 넣으면 "경고 메세지" 다시 입력
-> 0보다 작거나 100이상을 입력해도 "경고 메세지" 다시 입력
-> 정상 범위에 정수값을 입력하면 다음  단계 진행
'''

while True:
    your_number = str(input('AI의 숫자를 입력하세요?'))
    if not your_number:
        print('다시입력해')
    elif not your_number.isnumeric():
        print('야 숫자아니야')
    elif int(your_number) < 0 or int(ai_number) >=100:
        print('야 범위지켜') 
    else:
        break

'''
step 5
AI는 숫자를 하나 생성한다.(랜덤) -> 1회만 생성되어야함
즉 게임 한번이 종료될때가지 유지되어야 한다
'''
import random
ai_number = random.randint(0,99)

'''
step 6
판단 
1) 입력값이 정답보다 작으면  => 작다고 코멘트
2) 입력값이 정답보다 크면    => 크다고 코멘트
3) 입력값이 정답과 동일하면  => 축하메시지를 뿌려준다.
'''
while True:
    if your_number<ai_number:
        print('니가 입력한 숫자는 작어')
    elif your_number>ai_number:
        print('니가 입력한 숫자는 좀 크네?')
    else:
        print('축하해 맞췄어')