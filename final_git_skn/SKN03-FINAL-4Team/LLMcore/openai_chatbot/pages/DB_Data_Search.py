import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
import pandas as pd


# Page 1
st.title("Connection_test")
st.write("Welcome to Page 1! Use the buttons below to navigate.")

# 버튼 가로 배치
col1, col2, col3,_ = st.columns([1, 1, 1, 1])

# 버튼으로 페이지 이동
with col1:
    if st.button("Main Page"):
        switch_page("main")
with col2:
    if st.button("OpenAI LLM Model"):
        switch_page("openapi_model")
with col3:
    if st.button("Exaone LLM Model"):
        switch_page("exaone_model")


        
# Streamlit 제목
st.title("FastAPI와 Streamlit 간 송수신 테스트")

# 입력 폼 생성
name = st.text_input("이름 입력:")
value = st.number_input("값 입력:", min_value=0, step=1)

# 버튼 클릭 시 FastAPI로 데이터 송신
if st.button("전송", key="test_butten"):
    url = "https://backdocsend.jamesmoon.click/process/"  # FastAPI 엔드포인트 (fastapi url)
    payload = {"name": name, "value": value}  # 전송할 데이터
    try:
        # FastAPI로 POST 요청
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            # FastAPI 응답 출력
            st.success(f"응답: {response.json()}")
        else:
            st.error(f"에러: {response.status_code} - {response.json()}")
    except requests.exceptions.RequestException as e:
        st.error(f"요청 실패: {e}")
# FastAPI 엔드포인트 URL
POST_DELETE_BASE_URL = "https://backdocsend.jamesmoon.click/bizcontacts"  # FastAPI의 기본 URL

# Streamlit 타이틀 설정
st.title("BizContacts 정보 조회 및 관리")

# 선택 메뉴
option = st.selectbox("옵션 선택", ["조회: UUID", "조회: Order ID", "데이터 삭제: UUID", "데이터 삭제: Order ID"])

# 상태 관리를 위한 초기화
if "query_result" not in st.session_state:
    st.session_state.query_result = None  # 조회 결과 초기화

# null 값을 처리하는 헬퍼 함수
def sanitize_response(data):
    """응답 데이터의 null 값을 기본값으로 대체"""
    return {key: (value if value is not None else "정보 없음") for key, value in data.items()}


if option == "조회: UUID":
    # UUID로 데이터 조회
    uuid = st.text_input("UUID 입력:")
    if st.button("조회"):
        if uuid:
            try:
                response = requests.get(f"{POST_DELETE_BASE_URL}/uuid/{uuid}")
                if response.status_code == 201:
                    # 응답 데이터를 처리
                    result = response.json()
                    sanitized_result = sanitize_response(result)
                    st.session_state.query_result = sanitized_result  # 상태에 저장
                    st.success("조회 성공")
                else:
                    st.error(f"조회 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("UUID를 입력해주세요.")

    # 조회 결과 출력
    if st.session_state.query_result:
        st.write("조회 결과:")
        st.json(st.session_state.query_result)

elif option == "조회: Order ID":
    # Order ID로 데이터 조회
    order_id = st.text_input("Order ID 입력:")
    if st.button("조회"):
        if order_id:
            try:
                response = requests.get(f"{POST_DELETE_BASE_URL}/order_id/{order_id}")
                if response.status_code == 201:
                    # 응답 데이터를 처리
                    result = response.json()
                    sanitized_result = sanitize_response(result)
                    st.session_state.query_result = sanitized_result  # 상태에 저장
                    st.success("조회 성공")
                else:
                    st.error(f"조회 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("Order ID를 입력해주세요.")

    # 조회 결과 출력
    if st.session_state.query_result:
        st.write("조회 결과:")
        st.table(pd.DataFrame([st.session_state.query_result]))

elif option == "데이터 삭제: UUID":
    # UUID로 데이터 삭제
    uuid = st.text_input("UUID 입력:")
    if st.button("삭제"):
        if uuid:
            try:
                response = requests.delete(f"{POST_DELETE_BASE_URL}/uuid/{uuid}")
                if response.status_code == 201:
                    st.success("데이터 삭제 성공")
                    st.session_state.query_result = None  # 상태 초기화
                else:
                    st.error(f"삭제 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("UUID를 입력해주세요.")

elif option == "데이터 삭제: Order ID":
    # Order ID로 데이터 삭제
    order_id = st.text_input("Order ID 입력:")
    if st.button("삭제"):
        if order_id:
            try:
                response = requests.delete(f"{POST_DELETE_BASE_URL}/order_id/{order_id}")
                if response.status_code == 201:
                    st.success("데이터 삭제 성공")
                    st.session_state.query_result = None  # 상태 초기화
                else:
                    st.error(f"삭제 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("Order ID를 입력해주세요.")


# FastAPI 서버 URL
PUT_BASE_URL = "https://backdocsend.jamesmoon.click"  # FastAPI 서버의 기본 URL

# UUID 입력받기
st.title("Biz Contacts Update")
uuid = st.text_input("Enter the UUID of the record to update:")

# 폼(Form)을 사용해 수정할 데이터 입력받기
with st.form("update_form"):
    st.write("Fill in the fields to update (leave blank to skip):")
    service_name = st.text_input("Service Name")
    service_info = st.text_area("Service Info")
    budget = st.text_input("Budget")
    period = st.text_input("Period")
    platform = st.text_input("Platform")
    promo_info = st.text_area("Promo Info")
    service_target = st.text_area("Service Target")
    service_charactors = st.text_input("Service Charactors")

    # 폼 제출 버튼
    submitted = st.form_submit_button("Update Record")

# 폼이 제출되었을 때 처리
if submitted:
    # 수정할 데이터만 전송하기 위해 조건적으로 구성
    update_data = {
        "service_name": service_name if service_name else None,
        "service_info": service_info if service_info else None,
        "budget": budget if budget else None,
        "period": period if period else None,
        "platform": platform if platform else None,
        "promo_info": promo_info if promo_info else None,
        "service_target": service_target if service_target else None,
        "service_charactors": service_charactors if service_charactors else None,
    }

    # None 값을 제거하여 FastAPI에 필요한 데이터만 전송
    update_data = {k: v for k, v in update_data.items() if v is not None}
    
    st.write("Update Data:", update_data)  # 디버깅용 출력
    st.write("Request URL:", f"{PUT_BASE_URL}/bizcontacts/{uuid}")


    if update_data:
        if uuid:
            # FastAPI로 업데이트 요청 보내기
            try:
                response = requests.put(f"{PUT_BASE_URL}/bizcontacts/{uuid}", json=update_data)
                if response.status_code == 200:
                    st.success("Record updated successfully!")
                    st.json(response.json())  # 응답 데이터를 JSON 형식으로 출력
                else:
                    st.error(f"Failed to update record: {response.status_code}")
                    st.json(response.json())
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter a valid UUID.")
    else:
        st.error("No data to update. Please fill at least one field.")