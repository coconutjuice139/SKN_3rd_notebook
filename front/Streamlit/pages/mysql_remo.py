import streamlit as st
import pymysql
import pandas as pd

# Streamlit secrets에서 MySQL 연결 정보 가져오기
connection = st.secrets["mysql"]

# 데이터베이스에 연결
conn = pymysql.connect(
    host=connection["localhost"],
    user=connection["urstory"],
    password=connection["u1234"],
    database=connection["classicmodels"],
    port=connection.get("port", 3306)  # 포트가 명시되어 있지 않으면 기본 포트 3306 사용
)

# SQL 쿼리 정의
sql = '''
SELECT
    *
FROM orders
WHERE 1=1
LIMIT 10;
'''

# SQL 쿼리 실행 및 데이터프레임 생성
with conn.cursor() as cursor:
    cursor.execute(sql)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # 열 이름 가져오기
    df = pd.DataFrame(result, columns=columns)

# 연결 종료
conn.close()

# 데이터프레임을 Streamlit 앱에 표시
st.dataframe(df)
