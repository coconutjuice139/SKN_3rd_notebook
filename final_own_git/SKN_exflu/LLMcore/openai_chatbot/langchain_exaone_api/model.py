from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

@st.cache_resource(show_spinner=False)
def creat_chat_model(model_id:str="gpt-4o-mini", streaming = True, temperature=0):
    return ChatOpenAI(model=model_id, streaming=streaming, temperature=temperature)

def create_prompt():
    # 프롬프트 생성
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "당신의 이름은 AdI이며, IT관련 전문가입니다."),
        ("user", "{user_input}"),
    ])
    return chat_prompt