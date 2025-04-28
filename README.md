# SaHa10_Fucking_Bus_Arrive
Why can't we use Saha 10 bus normally

# Directory
```tree
saha10-bus-app/
├── packages/
│   ├── frontend/
│   └── backend/
│       ├── app/          # 주 애플리케이션 코드
│       │   ├── __init__.py
│       │   ├── main.py       # FastAPI 앱 실행 및 라우터 설정
│       │   ├── api/          # API 엔드포인트 (라우터)
│       │   │   ├── __init__.py
│       │   │   └── endpoints/
│       │   │       ├── __init__.py
│       │   │       └── bus_arrivals.py # 버스 도착 정보 관련 엔드포인트
│       │   ├── core/         # 설정 등 핵심 로직
│       │   │   ├── __init__.py
│       │   │   └── config.py   # API 키 등 설정 관리
│       │   ├── models/       # 데이터 모델 (Pydantic) 및 DB 모델 (선택)
│       │   │   ├── __init__.py
│       │   │   └── schemas.py  # Pydantic 스키마 (API 요청/응답 정의)
│       │   │   # ├── db.py   # (선택) SQLAlchemy 등 DB 모델 정의
│       │   ├── services/     # 비즈니스 로직, 외부 API 연동, 예측 로직
│       │   │   ├── __init__.py
│       │   │   ├── bims_service.py # BIMS API 연동 및 XML 처리 로직
│       │   │   └── prediction_service.py # 도착 시간 예측 로직
│       │   │   # ├── database_service.py # (선택) DB 로깅 로직
│       │   └── utils/        # 유틸리티 함수
│       │       ├── __init__.py
│       │       └── xml_parser.py # XML 파싱 헬퍼 함수
│       ├── tests/          # 백엔드 테스트 코드
│       ├── requirements.txt  # 백엔드 Python 종속성
│       └── .env            # (선택) 환경 변수 파일 (API 키 등 민감 정보)
└── ... (루트 파일들)