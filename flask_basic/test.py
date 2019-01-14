# 데이터가 덩어리채 온다(구분자(sep..)를 통해서)
datas = '1000/4/5/3/5/6/3/2'.split('/')
print(datas)
# 합산
# 하나씩 구성원을 뽑는다.
addSum = 0
for n in datas:
    addSum+=int(n)
print(addSum)

# 포맷팅에서 %를 문자로 인식하게 할려면 %%를 사용한다.
sql = '''
    select 
        *
    from 
        tbl_trade 
    where name like '%%%s%%';
'''
print(sql % '삼')

# 파이썬의 3항 연산자는 없어서 비슷하게 만드는게 3항식
# 타언어의 3항 연산자는 조건문 ? 값:값;
# cur나 rate면 "" 아니면 disabled
key = 'cur'
result = '' if key == 'cur' or key =='rate' else 'disabled'
print(result)