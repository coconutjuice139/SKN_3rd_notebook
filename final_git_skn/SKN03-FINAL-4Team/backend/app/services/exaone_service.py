from fastapi import HTTPException
from app.schemas.exaone import GenerateRequest
from app.common.config import OLLAMA_API_URL
import requests
import json
import httpx
import logging

def generate_ollama_exaone_service(payload: dict):
    """
    Ollama 서버에 스트리밍 요청을 보내고 'response' 필드를 실시간으로 yield 합니다.
    """
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        
        if response.status_code != 200:
            yield json.dumps({"error": "Failed to fetch response from Ollama server"})
            return
        
        for line in response.iter_lines():
            if line:  # 빈 줄 제외
                try:
                    data = json.loads(line.decode("utf-8"))  # 각 라인을 JSON으로 파싱
                    response_text = data.get("response", "")  # 'response' 필드 추출
                    yield response_text  # 청크 단위로 반환
                except json.JSONDecodeError:
                    continue  # JSON 파싱 에러는 무시
    except Exception as e:
        yield json.dumps({"error": str(e)})

logging.basicConfig(level=logging.DEBUG)

async def generate_stream(payload: dict):
    """
    Ollama 서버와의 스트리밍 통신 처리.
    JSON 데이터를 파싱하여 `response` 필드만 반환.
    """
    try:
        timeout = httpx.Timeout(10.0, read=20.0)  # 타임아웃 설정
        async with httpx.AsyncClient(timeout=timeout) as client:
            async with client.stream("POST", OLLAMA_API_URL, json=payload) as response:
                if response.status_code != 200:
                    raise HTTPException(status_code=response.status_code, detail=f"Error from Ollama server: {response.status_code}")
                async for line in response.aiter_text():
                    # 빈 줄 무시
                    if not line.strip():
                        continue
                    try:
                        # JSON 파싱 및 `response` 필드 추출
                        data = json.loads(line.strip())
                        if "response" in data and data["response"]:
                            logging.debug(f"Extracted response: {data['response']}")
                            yield data["response"]
                    except json.JSONDecodeError as e:
                        logging.error(f"Failed to decode JSON: {line.strip()}")
                        continue
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Streaming failed: {str(e)}")