import streamlit as st
from openai import OpenAI # API 통신용 모듈 
from langchain_common.chain import make_chain, runnable_parallel_chain, runnable_lambda_chain
import time

# @st.cache_data # 데이터를 caching 처리 
@st.cache_resource # 객체를 caching 처리 
def get_client():
    return OpenAI()



def response_from_langchain(prompt, message_history=[], model_id:str="gpt-4o-mini"):
    chain = make_chain(model_id)
    
    response_langchain = chain.invoke({prompt}, stream=True)
    
    # 스트리밍 데이터 반환 처리
    for chunk in response_langchain.content:
        if chunk is not None:
            yield chunk  # 여기서 chunk를 한 조각씩 반환
            time.sleep(0.01)
            
    message_history.append({"role": "assistant", "content": response_langchain.content})


def response_from_runnable_parallel(prompt, message_history=[], model_id:str="gpt-4o-mini"):
    combined = runnable_parallel_chain()
    
    response_runnable_langchian = combined.invoke({"country": prompt}, stream=True)
    for key in response_runnable_langchian.keys():
        for chunk in response_runnable_langchian[key].content:
            if chunk is not None:
                yield chunk  # 여기서 chunk를 한 조각씩 반환
                time.sleep(0.01)

    # message_history.append({"role": "assistant", "content": response_runnabel_langchain.content})

def response_from_runnable_lambda(prompt, message_history=[], model_id:str="gpt-4o-mini"):
    chain_runnable_lambda = runnable_lambda_chain()

    response_runnable_lambda = chain_runnable_lambda.invoke(prompt)
    
    for chunk in response_runnable_lambda.content:
        if chunk is not None:
            yield chunk  # 여기서 chunk를 한 조각씩 반환
            time.sleep(0.01)
    message_history.append({"role": "assistant", "content": response_runnable_lambda.content})