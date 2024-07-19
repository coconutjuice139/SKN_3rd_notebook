#########################################################
## join에 대해서 배워봅시다~~~~~~~~~~~~~ 분석가의 걸음마
#########################################################

-- 왼쪽을 기준으로 오른쪽 얘를 제거할 거다라고 생각해야 쉬워진다.
-- join은 결국 단순해야 한다.
-- 우리는 이제 왼쪽을 기준으로 A B의 set을 다룬다고 생각하고
-- Union을 제외하고 join을 할 때, A-B를 기준으로 inner(a, b)를 포함하냐 마냐의 판단

-- 이것만 외우고 ㄱㄱ
-- inner join : set A, set B 둘 다 가지고 있는 데이터
-- left join : set A의 원소들 set B의 원소로 빼서 set A에 남아있는 데이터(원소)
-- 일단 해보고 점점 에자일로 하다보면 점점 커진다
-- 보통 SQL join에서 data set을 지칭할 때 alias를 사용한다 ex) t1
-- ON 뒤에는 모집단을 작성한다.
-- 뒤에 where문을 통해 inner구간을 포함할지 안할지 결정한다.

-- set A, B는 상관관계가 있어야 join을 할 수 있다.

show tables;

desc customers;
desc orders;


#################
# left join -> contect key = cumstomerNumber -> 이거 join key가 되는 것 보통 ERD(1:N)에서 상위(1)의 개념을 선택

# 구매하지 않은 고객 리스트 조회 해당 코드는 기술적으로 접근하지 말 것 어떤 데이터를 뽑아내는 것이지 left join 할건데요 이건 잘못된 말
# set A -> customers
# set B -> orders

SELECT 
	cst.*
FROM customers cst
left join orders
on cst.customerNumber = orders.customerNumber  -- join 전 조건 필터링
WHERE 1=1                                      -- join 후 조건 필터링
	and orders.customerNumber IS NULL          -- 주문에서 비어있는 사람을 찾는다 = 주문을 하지 않은 사람을 찾는다.
;


-- 위의 구문을 하나의 데이터 셋이라 생각하고 from에 작성하고 on에 검증 data set을 들고 오면 된다.
-- 위는 set a에서 b와 중첩되는 구간을 제외한 a이다.
-- 따라서 b와 inner 또는 left join을 하면 데이터가 나오지 않게 된다.



# inner join -> contect key = cumstomerNumber -> 이거 join key가 되는 것 보통 ERD(1:N)에서 상위(1)의 개념을 선택

SELECT 
	a1.*
FROM (
	########################
	SELECT 
		a.*
	FROM customers a                       -- a를 불러오고
	left join orders b                     -- (a left join b) a와 b를 붙이는데 왼쪽을 기준으로 하여
	on a.customerNumber = b.customerNumber -- data set union (a, b)에서
	WHERE 1=1
		and b.customerNumber is null       -- a에 b를 갖다 붙임이고 왼쪽(a)을 기준으로 생각하는 a 데이터에서 column에 b데이터는 겹치지 않는 구간에 대해 null이 발생하고, 이 값을 제거하겠다. 
) a1
####################### --주문 안한 사람 데이터 셋
inner join orders b1
on a1.customerNumber = b1.customerNumber
where 1=1
	and b1.customerNumber is null
;


