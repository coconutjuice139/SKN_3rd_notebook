import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Main Application Page")
st.markdown("""LangChain Agent는 기본 LLM 기반의 모델에 검색엔진을 적용하였습니다. 
            따라서 원하는 답변을 받을 확률이 높으며 최신 정보도 얻을 수 있습니다.
            
            """)
            
st.markdown("""LangChain Chatbot은 기본 LLM모델 기반에 여행관련 자료에 특화된 모델입니다.
            여행과 관련된 답변에 전문화 되어 있으므로 여행관련 질문은 해당 모델을 사용하시면 됩니다.""")

page = st.sidebar.selectbox(
    "Select a page",
    ["streamlit_main_page", "langchain_agent", "langchain_chatbot"],  # "Select a page" 옵션 제거
    index=0  # streamlit_main_page를 기본 선택값으로 설정
)
# 페이지 이동
if page == "langchain_chatbot":
    switch_page("langchain_chatbot")
elif page == "langchain_agent":
    switch_page("langchain_agent")