from fastapi import APIRouter, Depends, HTTPException
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.exaone import GenerateRequest
from app.services.exaone_service import generate_ollama_exaone_service, generate_stream
from app.database.database import get_db
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/exaone", tags=["exaone"])

# 블로그 전체 조회


@router.post("/generate", summary="Ollama 송수신")
async def generate_streaming(request: GenerateRequest):
    """
    스트리밍 방식으로 LLM 응답 반환.
    """
    payload = {"model": request.model, "prompt": request.prompt}
    return StreamingResponse(generate_stream(payload), media_type="text/plain")

