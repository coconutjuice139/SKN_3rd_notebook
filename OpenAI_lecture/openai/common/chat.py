from msilib import MSIMODIFY_VALIDATE_FIELD
import streamlit as st 
from openai import OpenAI 
import openai
import time

# @st.cache_data # 데이터를 caching 처리
@st.cache_resource # 객체를 caching 처리 -> 아래의 OpenAI의 객체가 없으면 새로 만들고, 있으면 있던거 사용하기
def get_client():
    return OpenAI()

def response_from_llm(prompt, model_id:str='gpt-4o-mini'):
    streaming = get_client().chat.completions.create(
        model = model_id,
        messages = [
            {
                'role':'assistant',
                'content':'당신은 어시스턴트입니다.'
            },
            {
                'role':'user',
                'content':prompt
            }
        ],
        stream = True,
        max_tokens = 50
    )

    for chunk in streaming:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content
            time.sleep(0.05)
    # return responses.choices[0].message.content
    
def response_from_llm_img(prompt):
    response = get_client().images.generate(
        model = "dall-e-3", # 생성형 LLM model
        prompt = prompt, # 요청내용
        n = 1, # 생성 이미지 수
        size = "1024x1024", # 이미지 크기
        quality= "standard" # 생성될 이미지 품질
    )
    return response.data[0].url

def response_from_llm_text(prompt):
    response = get_client().chat.completions.create(
    model = "gpt-4o-mini",
    max_tokens= 300,
    messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": st.session_state.messages[-2]['content'] 
                            # 원래 값은 1이 입력되어 있었음, 입력을 받으면 입력이 -1이 되고 그 이전 봇의 답변이 -2가 된다.
                            # 또한 여러 질문이 들어가면 어떻게 되는지 생각도 해봐야 하것다.
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content