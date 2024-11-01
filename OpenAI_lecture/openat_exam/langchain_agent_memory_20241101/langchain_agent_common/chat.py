import streamlit as st
from langchain_openai import ChatOpenAI # API 통신용 모듈 
from langchain_agent_common.taviny_result import response_taviny_results
import time

# @st.cache_data # 데이터를 caching 처리 
@st.cache_resource # 객체를 caching 처리 
def get_client(model_id='gpt-4o-mini', temperature = 0):
    return ChatOpenAI(model_id, temperature)


def response_from_tiviny(prompt, message_history=[], model_id:str="gpt-4o-mini"):
    agent_executor = response_taviny_results()
    
    response = agent_executor.invoke({"input": prompt})
    
    # 스트리밍 데이터 반환 처리
    for chunk in response["output"]:
        if chunk is not None:
            yield chunk  # 여기서 chunk를 한 조각씩 반환
            time.sleep(0.01)
            
    message_history.append({"role": "assistant", "content": response["output"]})
