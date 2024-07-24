import streamlit as st

#secrets에서 [connections.mydb]라고 지정해서 그걸 불러오는 것, 따라서 네이밍을 달리하면 여러 DB를 불러올 수 있다.
#커넥션 객체 생성 성공!!

conn = st.connection('mydb', type='sql')#, autocommit=True) 

sql = '''
select
    *
from orders
where 1=1
limit 10
;
'''

# 커넥션 객체가 sql 쿼리를 들고가서 명령을 수행 timeout은 3600ms 내에 한다.
df = conn.query(sql)
st.dataframe()