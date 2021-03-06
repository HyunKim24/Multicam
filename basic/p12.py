# 반복문 for
# 지정된 횟수를 반복
# for each 방식 지원
# 전체 시퀀스데이터 덩어리에서 하나씩 꺼내서 처리하는 방식
a = [1,2,3,4,5]
for item in a:
    print(item)
else:
    print('정상적으로 반복문이 종료되었다')
####################################################################    
# break, continue 다 지원
####################################################################    
a = [(1,2),(3,4),(5,6),(7,8)]
# a에 있는 구성원들을 모두 출력하시오. 출력 모양은 자유롭게
for item in a:
    print(item[0],item[1])
# 구성원이 튜플인 경우 튜플의 멤버수대로 바로 
# 변수에 받을 수 있다.
for i,j in a:
    print(i,j)
####################################################################
a = {
    'name':'multi',
    'age':10
}
# 값만 출력하시오
# 딕셔너리를 그냥 for문으로 돌리면 키만 나온다.
for key in a:
    print(key, a[key])
# 값만 모아서 추력 => 유용성은 ???
for v in a.values():
    print(v)
####################################################################
# 연속수 출력
# range() 연속된 수를 생성
# 0 <= n <10
for n in range(10):
    print(n)
# 1 <= n < 5
for n in range(1,5):
    print(n)
####################################################################
# range()를 이용하여 구구단 구성
# 3단~6단까지 구구단을 구성하시오
# 출력 형태는 3 x 1 = 3...  6 x 9 = 54
####################################################################
tmp = list()
for i in range(3,7):
    for j in range(1,10):
        # 곱한 값만 모은다. => 리스트에 담아라
        # print(i*j)
        tmp.append(i*j)
        # print("%s x %s = %2s" %(i,j,i*j))
print(tmp)
####################################################################
# 리스트 내포
print( "="*50)
a = [i*j for i in range(3,7) for j in range(1,10)]
print(a)
