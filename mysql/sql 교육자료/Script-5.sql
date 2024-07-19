show tables;

SELECT * FROM customers;

-- insert = row가 증가

SELECT * FROM customers
limit 10; -- 전체 데이터 중 10개만 뽑아 본다 (순차적임)




SELECT  -- 몇몇 column만 뽑아보기
	customerNumber
	, contactFirstName 
	, city 
	, state 
	, postalCode 
	, country 
from customers
; -- 새로운 데이터 셋이 리턴되었다고 생각하면 된다.

-- 모든 데이터를 보면 insight를 찾기 어려움
-- 전체가 아닌 어떤 데이터를 뽑아서 보면 insight를 찾기 수월해진다.
-- 따라서 일부 데이터를 통해서 insight를 찾는 것이 좋다.

-- 위의 데이터 셋에 새로운 규칙을 집어 넣어서 표현해 보자

SELECT  -- 몇몇 column만 뽑아보기
	t1.*
from (  -- 괄호 무조건 넣어라
	SELECT  -- 몇몇 column만 뽑아보기
		customerNumber
		, contactFirstName 
		, city 
		, state 
		, postalCode 
		, country 
	from customers -- 이구간이 새로운 데이터 셋이니 from data가 가능
) t1 -- 알리아스: 가상의 테이블로 정의 즉, 선 조건으로 뽑아낸 데이터셋의 명명이라고 생각하면 된다.
WHERE 1=1
and t1.country = 'USA'  -- t1의 나라가 USA인 것만 뽑아줘 view table과 동일한 원리이다.
;

#####################################################################################

SELECT  -- 몇몇 column만 뽑아보기
	  t1.city
	, t1.state
	, t1.country  -- 아래의 select의 범위 column 내에서만 선택 가능하다.
from (  -- 괄호 무조건 넣어라
	SELECT  -- 몇몇 column만 뽑아보기
		  customerNumber
		, contactFirstName 
		, city 
		, state 
		, postalCode 
		, country 
	from customers -- 이구간이 새로운 데이터 셋이니 from data가 가능
	WHERE 1=1
) t1 -- 알리아스: 가상의 테이블로 정의 즉, 선 조건으로 뽑아낸 데이터셋의 명명이라고 생각하면 된다.
WHERE 1=1
and t1.country = 'USA'  -- t1의 나라가 USA인 것만 뽑아줘 view table과 동일한 원리이다.
;


#######################################################################



SELECT
	  t1.customer_number -- as를 넣으면 as로 선정한 이름으로 집어넣어줘야 한다.
	, t1.contact_first_name  -- as를 넣으면 as로 선정한 이름으로 집어넣어줘야 한다.
	, t1.country
from (
	SELECT
		  customerNumber as customer_number
		, contactFirstName as contact_first_name
		, city 
		, state 
		, postalCode 
		, country 
	from customers
	WHERE 1=1
) t1
WHERE 1=1
and t1.country = 'USA'
;