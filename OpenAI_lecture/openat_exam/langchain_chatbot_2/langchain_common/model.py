from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def creat_chat_model(model_id:str="gpt-4o-mini"):
    return ChatOpenAI(model=model_id)

def create_prompt():
    # 프롬프트 생성
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "이 시스템은 여행 전문가입니다."),
        ("user", "{user_input}"),
    ])
    return chat_prompt