from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from typing import Optional, List
from langchain.base_language import BaseLanguageModel
import httpx
from pydantic import Field


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

class FastAPILLM(BaseLanguageModel):
    api_url: str = Field(..., description="The URL of the FastAPI server")
    model_name: str = Field(..., description="The name of the model to be used")

    @property
    def _llm_type(self) -> str:
        return "fastapi_llm"

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        LangChain에서 _call 메서드 호출을 처리합니다.
        """
        payload = {"model": self.model_name, "prompt": prompt}
        try:
            result = ""
            with httpx.stream("POST", self.api_url, json=payload) as response:
                if response.status_code != 200:
                    raise ValueError(f"Streaming failed with status code {response.status_code}")
                for chunk in response.iter_text():
                    if chunk:
                        result += chunk
            return result
        except Exception as e:
            raise ValueError(f"FastAPI call failed: {e}")

    def invoke(self, input: str, **kwargs) -> str:
        """
        LangChain에서 사용되는 invoke 메서드. FastAPI 서버로 요청을 전송하고 응답을 반환합니다.
        """
        return self._call(prompt=input, **kwargs)

    def predict(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        동기 방식으로 입력에 대한 예측을 반환합니다.
        """
        return self._call(prompt, stop, **kwargs)

    def apredict(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        비동기 방식으로 입력에 대한 예측을 반환합니다.
        """
        return self._call(prompt, stop, **kwargs)

    def generate_prompt(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        입력 데이터를 기반으로 프롬프트를 생성합니다.
        """
        return prompt

    def agenerate_prompt(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        비동기 방식으로 프롬프트를 생성합니다.
        """
        return self.generate_prompt(prompt, stop, **kwargs)

    def predict_messages(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        메시지 기반 입력에 대한 예측을 반환합니다.
        """
        return self._call(prompt, stop, **kwargs)

    def apredict_messages(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """
        메시지 기반 입력에 대한 비동기 예측을 반환합니다.
        """
        return self.predict_messages(prompt, stop, **kwargs)