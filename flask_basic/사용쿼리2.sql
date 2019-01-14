-- select * from tbl_trade where code='012330';
# 수정하기
-- update 테이블명 set 컬럼명=값, 컬럼명=값 .. 
-- where 조건식;
-- update tbl_trade set cur='2', rate='2.1' where code='012330';

-- select * from tbl_trade where code='012330';

# 삭제하기
-- delete from 테이블명 where 조건식;
select * from tbl_trade where code='012330';
delete from tbl_trade where code='012330';
select * from tbl_trade where code='012330';