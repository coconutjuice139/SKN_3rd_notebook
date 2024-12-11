from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine



DATABASE_URL = "mysql+asyncmy://admin:root12#$@influencerdb.c18uiyu26mws.ap-northeast-2.rds.amazonaws.com:3306/finaldatabase"

# 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# AsyncSession 생성
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)






# # 데이터베이스 엔진을 생성합니다.
# engine = create_engine(URL_DATABASE)

# # 세션 로컬을 생성합니다. autocommit과 autoflush를 False로 설정하여 수동으로 트랜잭션을 관리합니다.
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 선언적 기본 클래스를 생성합니다. 이 클래스를 상속하여 데이터베이스 모델을 정의합니다.
Base = declarative_base()

# from databases import Database

# # RDS 엔드포인트 및 연결 정보
# DATABASE_URL = "mysql+asyncmy://admin:root12#$@influencerdb.c18uiyu26mws.ap-northeast-2.rds.amazonaws.com:3306/finaldatabase"

# # 데이터베이스 객체 생성
# database = Database(DATABASE_URL)

# # 데이터베이스 연결 및 해제 함수
# async def connect_db():
#     await database.connect()

# async def disconnect_db():
#     await database.disconnect()
