# SKN03-FINAL-4Team Backend

## 기술 스택

### 주요 프레임워크 및 라이브러리
- **FastAPI**: 고성능 비동기 웹 프레임워크
  - CORS 미들웨어 지원
  - 세션 관리
  - 로깅 미들웨어
  - OpenAPI (Swagger) 문서 자동 생성
- **SQLAlchemy**: Python SQL 툴킷 및 ORM
  - 비동기 데이터베이스 작업 지원
  - 모델 기반 데이터베이스 관리
- **Uvicorn**: 고성능 ASGI 서버
- **Pydantic**: 데이터 검증 및 설정 관리
- **OpenAI**: AI 기능 구현
  - GPT 모델 통합
  - AI 기반 컨텐츠 생성

### 데이터베이스
- **MySQL**: 메인 데이터베이스
  - asyncmy: 비동기 MySQL 드라이버
  - pymysql: 동기 MySQL 드라이버
  - 트랜잭션 관리
  - 연결 풀링

### 인증 및 보안
- **소셜 로그인**:
  - Google OAuth2.0 인증
  - Kakao OAuth 인증
- **JWT**: JSON Web Token 기반 인증
  - PyJWT
  - python-jose
- **Passlib**: 비밀번호 해싱 (bcrypt)
- **Session Middleware**: 세션 기반 상태 관리

### 클라우드 및 인프라
- **AWS 서비스**:
  - AWS SDK (boto3)
  - AWS CodeBuild
  - CI/CD 파이프라인
- **Docker**: 컨테이너화
  - 멀티스테이지 빌드
  - 환경 변수 관리

### 개발 도구
- **Loguru**: 구조화된 로깅
  - 로그 레벨 관리
  - 로그 포맷팅
  - 파일 로깅
- **Pytest**: 테스트 프레임워크
- **Python-dotenv**: 환경 변수 관리

## 프로젝트 구조

```
backend/
├── app/                    # 메인 애플리케이션 디렉토리
│   ├── auth/              # 인증 관련 모듈
│   │   ├── token.py      # JWT 토큰 관리
│   │   └── oauth.py      # OAuth 인증
│   ├── common/            # 공통 유틸리티
│   │   └── utils.py      # 유틸리티 함수
│   ├── database/          # 데이터베이스 설정 및 모델
│   │   ├── database.py   # DB 연결 설정
│   │   └── models.py     # SQLAlchemy 모델
│   ├── router/           # API 엔드포인트
│   │   ├── blog.py      # 블로그 관련 API
│   │   ├── sns.py       # SNS 통합 API
│   │   ├── core.py      # 핵심 기능 API
│   │   ├── biz_info.py  # 비즈니스 정보 API
│   │   ├── google_auth.py # Google 인증
│   │   └── kakao_auth.py  # Kakao 인증
│   ├── schemas/          # Pydantic 모델/스키마
│   ├── services/         # 비즈니스 로직
│   ├── main.py          # 애플리케이션 진입점
│   ├── logger.py        # 로깅 설정
│   └── settings.py      # 환경 설정
├── requirements.txt      # 의존성 패키지 목록
├── Dockerfile           # Docker 빌드 설정
└── buildspec.yml        # AWS CodeBuild 설정
```

## API 엔드포인트

### 1. 인증 관련
- `/auth/google`: Google OAuth2.0 인증
- `/auth/kakao`: Kakao OAuth 인증
- `/auth/token`: JWT 토큰 발급/갱신

### 2. 비즈니스 기능
- `/blog`: 블로그 관련 CRUD 작업
- `/sns`: SNS 통합 및 관리
- `/biz-info`: 비즈니스 정보 관리
- `/biz-contacts`: 비즈니스 연락처 관리

### 3. 시스템 관리
- `/healthcheck`: 시스템 상태 확인
- `/process-check`: 프로세스 모니터링
- `/core-check`: 핵심 기능 상태 확인

## 주요 기능

1. **API 서버**
   - RESTful API 설계
   - 비동기 처리
   - 미들웨어 기반 로깅
   - CORS 지원

2. **데이터베이스 관리**
   - ORM 기반 데이터 모델링
   - 비동기 쿼리 처리
   - 트랜잭션 관리
   - 마이그레이션 지원

3. **인증 시스템**
   - 소셜 로그인 (Google, Kakao)
   - JWT 기반 인증
   - 세션 관리
   - 보안 토큰 관리

4. **로깅 시스템**
   - 구조화된 로그 관리
   - 요청/응답 로깅
   - 에러 트래킹
   - 성능 모니터링

5. **AI 통합**
   - OpenAI API 활용
   - 컨텐츠 생성
   - 자연어 처리

6. **클라우드 통합**
   - AWS 서비스 연동
   - 클라우드 스토리지 관리
   - 서버리스 기능 통합

## 설치 및 실행

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 환경 변수 설정:
`.env` 파일 생성:
```env
DATABASE_URL=mysql+asyncmy://user:password@localhost:3306/dbname
JWT_SECRET_KEY=your-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
KAKAO_CLIENT_ID=your-kakao-client-id
OPENAI_API_KEY=your-openai-api-key
```

3. 데이터베이스 설정:
```bash
# MySQL 데이터베이스 생성
mysql -u root -p
CREATE DATABASE dbname;
```

4. 서버 실행:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 배포

### Docker 배포
```bash
# 이미지 빌드
docker build -t backend-app .

# 컨테이너 실행
docker run -d -p 8000:8000 --env-file .env backend-app
```

### AWS 배포
- CodeBuild를 통한 자동 배포
- `buildspec.yml`에 정의된 파이프라인 실행
- 환경 변수는 AWS Systems Manager Parameter Store에서 관리

## 모니터링

- 헬스체크 엔드포인트: `/healthcheck`
- 프로세스 모니터링: `/process-check`
- 로그 확인: `app.log` 파일
- AWS CloudWatch 통합 모니터링