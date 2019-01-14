-- 테이블 삭제
# drop table tbl_fileBbs;

-- 데이터 추가
insert into 
	tbl_filebbs
(`title`,`content`,`author`,`files`)
	values
('1','2','m','Desert.jpg');

select * from tbl_filebbs order by id desc limit 10;