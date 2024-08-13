show tables; -- 테이블 보기

desc customers; -- description의 약자로 스키마 정보를 볼 수 있다.

SELECT  -- * 요거보단 실제 column명을 넣어서 작동시키기 나중에 주석처리로 예외시키면 되니까
	  customerName as cust_nm -- 알리아스(alias:약어, 별칭) cust는 일반적으로 customer일 확률이 매우 높음
	, phone
	, city
	, country
	, creditLimit
from customers -- table 명
WHERE 1=1  -- 조건식 넣을 준비(이건 조건이 없어도 습관화)
LIMIT 10  -- 결과를 상위 10개만 내오기
; 


#################################################################
# 위의 데이터셋을 from에 집어 넣고 알리아스를 지정하여 다시 데이터를 추출해보자
#################################################################



SELECT 
	  t1.*  -- from부의 데이터 셋의 alias를 앞에 작성하고 .으로 어떤데이터를 불러올지 지정한다. *를 누르면 모든 데이터를 의미한다.
from( 
	SELECT  -- * 요거보단 실제 column명을 넣어서 작동시키기 나중에 주석처리로 예외시키면 되니까
		  customerName as cust_nm -- 알리아스(alias:약어, 별칭) cust는 일반적으로 customer일 확률이 매우 높음
		, phone
		, city
		, country
		, creditLimit as credit_limit
	from customers -- table 명
	WHERE 1=1  -- 조건식 넣을 준비(이건 조건이 없어도 습관화)
		and country = 'Australia' -- 나라를 오스트렐리아로 변경
--	ORDER BY creditLimit DESC -- where절은 from의 원본 column명을 해줘야 한다. 위의 as를 따르지 않는다. (내림차순: DESC/descending order, 오름차순 ASC/ascending order) 
--	LIMIT 10  -- 결과를 상위 10개만 내오기
) t1 -- 콜론 넣지말고 그냥 alias(별칭)만 넣고 데이터 셋으로 집어넣자
where 1=1
--	and credit_limit > 100000 -- 이 기준에 부합하는 결과를 불러와달라.
LIMIT 10                      -- 위의 데이터 셋을 기준으로 리미트로 10명을 불러오지만 그 결과가 10명이 안되면 그 아래 숫자로 결과를 보여준다.
                              -- 실제 고객이 credit_limit이 넘는 사람은 많겠지만 위의 데이터 셋이 10명으로 제한했기 때문에 그 영향이 이후 쿼리에도 영향을 준다.
;



#####################################################################################################################33
## join 데이터 조회 -> 쿼리를 잘하는지, 좋아하는지의 경계선
########################################################################################################################

-- 쉬워지는 팁으로 right join을 생각하지 말자
