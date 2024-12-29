# app/auth/token.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.common.config import get_parameter
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


SECRET_KEY = get_parameter("/MYAPP/GOOGLE/AUTH/SECRETKEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Google과 Kakao의 OAuth2PasswordBearer 각각 정의
google_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/google")
kakao_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/kakao")


# Google과 Kakao의 SECRET_KEY
GOOGLE_SECRET_KEY = get_parameter("/MYAPP/GOOGLE/AUTH/SECRETKEY")
KAKAO_SECRET_KEY = get_parameter("/MYAPP/GOOGLE/AUTH/SECRETKEY")

# 토큰 검증 함수
def verify_access_token(token: str, secret_key: str):
    try:
        # JWT 디코딩
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        # 토큰 만료 여부 확인
        exp = payload.get("exp")
        if exp and datetime.utcnow().timestamp() > exp:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# 동적으로 Google 또는 Kakao 인증 처리
def get_current_user(
    google_token: str = Depends(google_oauth2_scheme), kakao_token: str = Depends(kakao_oauth2_scheme)
):
    try:
        # Google 인증 처리
        try:
            payload = verify_access_token(google_token, GOOGLE_SECRET_KEY)
            user_email = payload.get("sub")
            if not user_email:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Google token does not contain user email",
                )
            return {"email": user_email, "provider": "google"}
        except HTTPException as google_exception:
            # Google 검증 실패 시 Kakao로 전환
            if google_exception.detail == "Token expired":
                # Google 토큰 만료 예외는 그대로 반환
                raise google_exception
            # Google 검증 실패는 무시하고 Kakao 검증으로 넘어감
            pass

        # Kakao 인증 처리
        payload = verify_access_token(kakao_token, KAKAO_SECRET_KEY)
        user_email = payload.get("sub")
        if not user_email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Kakao token does not contain user email",
            )
        return {"email": user_email, "provider": "kakao"}
    except HTTPException as e:
        # 토큰 만료 예외 처리
        if e.detail == "Token expired":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="토큰이 만료되었습니다. Refresh Token을 사용하여 새 Access Token을 요청하세요.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # 기타 인증 실패 예외 반환
        raise e
    except Exception:
        # 유효하지 않은 토큰 또는 기타 예외 처리
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 토큰입니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )


# Access Token 생성 함수
def create_access_token(data: dict, provider: str):
    """
    Access Token 생성
    """
    to_encode = data.copy()
    to_encode["provider"] = provider
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    secret_key = GOOGLE_SECRET_KEY if provider == "google" else KAKAO_SECRET_KEY
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)

# Refresh Token 생성 함수
def create_refresh_token(data: dict, provider: str):
    """
    Refresh Token 생성
    """
    to_encode = data.copy()
    to_encode["provider"] = provider
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    secret_key = GOOGLE_SECRET_KEY if provider == "google" else KAKAO_SECRET_KEY
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)