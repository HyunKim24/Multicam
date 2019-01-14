import random

'''
step 1
"게임의 제목을 입력하세요" 프럼프트 출력
"적당한 제목(영문)" 입력하면 다음 단계 진행
'''

gameTitle = input('게임의 제목을 입력하세요\n')

'''
step 2
===========================
=     게임제목(중앙정렬)   = 
=     v 1.0.0             =
===========================
이렇게 출력
'''
TITLE_LEN = 30
print('='*TITLE_LEN)
txt = '={0:^%s}=' %(TITLE_LEN-2)
data = [gameTitle,'V 1.0.0']
for i in data:
    print(txt.format(i))
print('='*TITLE_LEN)

'''
step 3
게이머의 이름을 입력하세요?
-> 이름을 넣지 않으면 "뭐라뭐라 하고" 다시 입력
'''
while True:
    gamePlayer = input('게이머의 이름을 입력하세요?\n')
    if not gamePlayer:
        print('이름을 입력하세요!!')
    else:
        break

'--------스텝 4 6 7은 한곳으로 짬뽕---------'

'''
step 4
AI의 숫자를 입력하세요?
-> 숫자를 안넣으면 "경고 메세지" 다시 입력
-> 숫자가 아닌 값을 넣으면 "경고 메세지" 다시 입력
-> 0보다 작거나 100이상을 입력해도 "경고 메세지" 다시 입력
-> 정상 범위에 정수값을 입력하면 다음  단계 진행
'''
'''
step 6
판단 
1) 입력값이 정답보다 작으면  => 작다고 코멘트
2) 입력값이 정답보다 크면    => 크다고 코멘트
3) 입력값이 정답과 동일하면  => 축하메시지를 뿌려준다.
'''
'''
step 7
결과 표시
총 시도 횟수 표시
점수 = (10-총시도횟수)*10 를 표시
다시 게임을 하시겠습니까?
YES(대소문자 구분 안함) => 다시 게임 시작(step 4부터 진행)
No(대소문자 구분 안함) => 게임 종료 => 프로그램 종료
아무것도 안넣고 엔터 => 경고 메시지
입력값이 틀려도 경고

'''
flag1 = True

while flag1:
    AI = random.randint(0,99)
    trycount = 0
    while True:
        print(AI)
        yourNum = input('AI에 숫자를 입력하세요?')
        if not yourNum:
            print('숫자를 입력해 주세요')
            trycount+=1
        elif not yourNum.isnumeric():
            print('숫자가 아닌 값을 입력하셨습니다.')
            trycount+=1
        elif int(yourNum) < 0 or int(yourNum) > 100:
            print('범위가 일치하지 않습니다.')
            trycount+=1
        else:
            if int(yourNum) < int(AI):
                print('입력값이 정답보다 작습니다. 다시 입력해 주세요')
                trycount+=1
            elif int(yourNum) > int(AI):
                print('입력값이 정답보다 큽니다. 다시 입력해 주세요')
                trycount+=1
            else:
                print('축하합니다. 정답입니다.')
                print('='*30)
                print('당신의 결과는 다음과 같습니다.')
                print('총 시도 횟수 : ',trycount)
                print('점수 : ',(10-trycount)*10)
                print('='*30)
                reset = input('계속할래?')
                if reset == 'YES':
                    break
                elif reset == 'NO':
                    flag1 = False
                    break
                    

