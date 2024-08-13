CREATE database customer;

show databases;

-- refresh 필수
use customer;

-- DB 내부 table들 목록 확인
show tables;

# 학생 student
create table student (
	student_id INT UNSIGNED auto_increment COMMENT '학생아이디',
	student_name varchar(10) not null COMMENT '학생이름',
	student_address varchar(50) null COMMENT '학생집주소',
	create_dt TIMESTAMP not null default now() COMMENT '생성일자',
	modify_dt TIMESTAMP not null default now() COMMENT '수정일자',
	PRIMARY KEY(student_id)
);

show tables;

show tables;


# 교수 professor
create table professor (
	professor_id INT UNSIGNED auto_increment COMMENT '교수아이디',
	professor_name varchar(10) not null COMMENT '교수이름',
	create_dt TIMESTAMP not null default now() COMMENT '생성일자',
	modify_dt TIMESTAMP not null default now() COMMENT '수정일자',
	PRIMARY KEY(professor_id)
);

commit;

show tables;


# 과목 subject
create table subject (
	subject_cd varchar(10) COMMENT '과목코드',
	subject_name varchar(10) not null unique COMMENT '과목명',
	subject_desc text COMMENT '과목설명',
	professor_id INT unsigned not null COMMENT '교수아이디',
	create_dt TIMESTAMP not null default now() COMMENT '생성일자',
	modify_dt TIMESTAMP not null default now() COMMENT '수정일자',
	PRIMARY KEY(subject_cd),
	FOREIGN KEY (professor_id) REFERENCES professor(professor_id) ON UPDATE CASCADE
);

# 수강신청 enrolment
create table enrolment (
	enrolment_id INT UNSIGNED auto_increment COMMENT '수강신청아이디',
	semester varchar(10) not null COMMENT '학기',
	student_id INT unsigned not null COMMENT '학생아이디',
	subject_cd varchar(10) not null COMMENT '과목코드',
	create_dt TIMESTAMP not null default now() COMMENT '생성일자',
	modify_dt TIMESTAMP not null default now() COMMENT '수정일자',
	PRIMARY KEY(enrolment_id),
	FOREIGN KEY (student_id) REFERENCES student(student_id) ON UPDATE cascade,
	FOREIGN KEY (subject_cd) REFERENCES subject(subject_cd) ON UPDATE CASCADE
);

commit;

show tables;

desc enrolment;


-- 만들어진 table에 column 추가 (테이블 수정)

alter table enrolment add column room_number int not null;

desc enrolment 


-- 만들어진 table에 column 수정

alter table enrolment modify column room_number varchar(10) null;


desc enrolment;


alter table enrolment change column room_number room_name varchar(50) not null;

desc enrolment ;

alter table enrolment drop column room_name;

desc enrolment ;















