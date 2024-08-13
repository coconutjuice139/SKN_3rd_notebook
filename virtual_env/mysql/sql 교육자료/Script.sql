show databases;

use mysql;

-- 사용자 확인하기

SELECT * from user;


-- 아이디 스키마 정보 보기

desc user; 

-- 사용자 계정 생성하기

CREATE user 'usercolumn'@hostcolumn identified by 'password';
CREATE user 'user_id'@localhost identified by 'password';
CREATE user 'user_id2'@'%' identified by 'password';


select * from user;

-- 비번 변경

set password for 'user_id2'@'%' = 'password2';


-- userid에게 exampledb 권한 부여하기
-- mysql > databases > tables > data
-- grant <data 조작권한, database범위, table 권한> to <user>;
grant ALL privileges on *.* to 'user_id2'@'%';

show databases;

use mysql;

grant select on examplesdb.* to 'user_id2'@'%';


CREATE user 'user1'@'%' identified by '123123';

grant select on examplesdb.* to 'user1'@'%';

SELECT * from user;


create user 'userid3'@'%' identified by 'userid1234'; 
grant select on examplesdb.* to 'userid3'@'%'; 
FLUSH PRIVILEGES; # 새로운 권한 MySQL 적용!!!

SELECT * from user;

drop user 'user1'@'%';
drop user 'user_id'@localhost;
drop user 'user_id2'@'%';
drop user 'userid3'@'%';


-- mysql > databases > tables > data

