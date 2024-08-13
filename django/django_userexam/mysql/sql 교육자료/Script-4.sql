####################################3
# 데이터 베이스 만들기
####################################3

CREATE database classicmodels;

show databases;

######################################3
#테이블 생성
######################################3

# DB 선택
use classicmodels;

CREATE table mytable (
id int unsigned auto_increment,
name varchar(50) not null,
model_number varchar(10) not null,
series varchar(30) not null,
primary key(id)
) ;


show tables;

desc mytable ;

select * from mytable;

select name, id, series from mytable;



-- 데이터 생성(입력)

-- dml은 유저 계정이 한다
-- 유저한테 권한을 줘보다

use mysql;

select * from user;

grant ALL privileges on classicmodels.* to 'urstory'@'%';
flush privileges;


-- urstory로 계정 전환함
use classicmodels;


insert into mytable(name, model_number, series) values('name1', 'number1', 'series1');

SELECT * from mytable ;

insert into mytable(name, model_number, series) values('name2', 'number2', 'series2');
insert into mytable(name, model_number, series) values('name3', 'number3', 'series3');
insert into mytable(name, model_number, series) values('name4', 'number4', 'series4');
insert into mytable(name, model_number, series) values('name5', 'number5', 'series5');
insert into mytable(name, model_number, series) values('name6', 'number6', 'series6');
insert into mytable(name, model_number, series) values('name7', 'number7', 'series7');

SELECT * FROM mytable;


SELECT             -- 명령문
	*                  -- 조회 컬럼 ....(조회 하고 싶은 컬럼을 지정해서 작성하면 된다.)
FROM mytable       -- 테이블
WHERE 1=1          -- 조건 (where 뒤에 1=1은 아래에 and, or 조건을 취사 선택이 많이 바뀐다. 따라서 주석처리를 통해 줬다 뺐다가 수월하게 가능 또한 where 바로 뒤에는 주석 처리가 안된다.)
	and id >3
	-- and name like '&name'
	-- and id < 7
	-- and series like 'series4'
;                   -- 세미 클론은 따로 맨 아래에 둠으로써 주석처리로 인해 발생하는 실행문 누락을 방지할 수 있다.



SELECT             -- 명령문
	name
	, id           -- 콤마는 앞에 달자
	, model_number -- 조회 컬럼 ....(조회 하고 싶은 컬럼을 지정해서 작성하면 된다.)
FROM mytable       -- 테이블
WHERE 1=1          -- 조건 (where 뒤에 1=1은 아래에 and, or 조건을 취사 선택이 많이 바뀐다. 따라서 주석처리를 통해 줬다 뺐다가 수월하게 가능 또한 where 바로 뒤에는 주석 처리가 안된다.)
	and id >3
	-- and name like '&name'
	-- and id < 7
	-- and series like 'series4'
;                   -- 세미 클론은 따로 맨 아래에 둠으로써 주석처리로 인해 발생하는 실행문 누락을 방지할 수 있다.


-- update로 date 수정하기 --

SELECT * FROM mytable;

UPDATE mytable 
SET model_number ='model1'
WHERE 1=1
	AND id = 6
	AND name = 'name6'
;

commit;

-- data 삭제해보기

DELETE FROM mytable 
WHERE 1=1
	AND name = 'name3'
;

SELECT * FROM mytable;


SELECT * FROM mytable;