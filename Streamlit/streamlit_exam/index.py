import streamlit as st

# streamlit 멀티 페이지 만드는 법

st.title('Multi Page Link')
st.page_link("./index.py", label="Home", icon="🏠")
st.page_link("./pages/text.py", label="Page 1", icon="1️⃣")
st.page_link("./pages/dataframe.py", label="Page 2", icon="2️⃣")
st.page_link("./pages/mysql.py", label="MySQL", icon="🌎")
# st.page_link("http://www.google.com", label="Google", icon="🌎")