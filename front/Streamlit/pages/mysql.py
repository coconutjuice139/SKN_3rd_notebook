import streamlit as st
import pymysql
import pandas as pd

# Streamlit secrets에서 MySQL 연결 정보 가져오기
connection = st.secrets["connections"]["mydb"]

# 연결 정보 출력 (보안을 위해 실제 배포 시 제거해야 함)
st.write(f"Connecting to MySQL server at {connection['host']} as {connection['user']}")

# 연결 시도
try:
    conn = pymysql.connect(
        host=connection["host"],
        user=connection["user"],
        password=connection["password"],
        database=connection["database"],
        port=connection.get("port", 3306)  # 포트가 명시되어 있지 않으면 기본 포트 3306 사용
    )
    st.write("Connected to the database successfully.")
except Exception as e:
    st.error(f"Error connecting to the database: {e}")

# SQL 쿼리 실행 및 데이터프레임 생성
try:
    sql = '''
    SELECT
        *
    FROM orders
    WHERE 1=1
    LIMIT 10;
    '''

    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]  # 열 이름 가져오기
        df = pd.DataFrame(result, columns=columns)

    # 연결 종료
    conn.close()
    st.write("Query executed successfully.")
    st.dataframe(df)
except Exception as e:
    st.error(f"Error executing query: {e}")
