import time
import pymysql
import streamlit as st
import pandas as pd
import os

def get_con():
    con = pymysql.connect(host='compose-mysql-db', 
                          user='root', 
                          password='root1234', 
                          charset='utf8') # 한글처리 (charset = 'utf8')
    # mysql, python app이 들어가서 서로 통신해야 하는데 커넥션 객체를 통해 연결이 되는데 보통 host는 ip가 들어가는데
    # 컨테이너를 올릴 때마다 ip가 바뀐다 -> 올라가기 전에 물리적으로 알 수 없음
    # 그래서 docker compose는 container 이름을 써넣고, 그 container가 하나의 네트워크 안에 있다면
    # 알아서 ip를 따라가서 통신이 된다.
    return con

def show_databases():
    con = None
    cur = None
    try:
        con = get_con()
        cur = con.cursor(pymysql.cursors.DictCursor)
        sql = "show databases"
        cur.execute(sql)

        rows = cur.fetchall()
        print("show databases is >> ")
        print(rows)
    except Exception as e:
        print("Exception > "+str(e))
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__== "__main__":
    print ("Sleep 5 seconds from now on...")
    time.sleep(5) # mysqldb가 생성될 시간동안 대기.....
    
    print("[Docker Compose][main] Start!!")
    show_databases()
    print("[Docker Compose][main] End!!")
    run()
    