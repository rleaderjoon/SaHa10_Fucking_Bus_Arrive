from pydantic_settings import BaseSettings
import os

# .env 파일이 있다면 환경 변수를 로드 (python-dotenv 설치 필요: pip install python-dotenv)
# from dotenv import load_dotenv
# load_dotenv()

class Settings(BaseSettings):
    BIMS_API_KEY: str

    # (선택) DB 연결 정보 등 추가 설정
    # DATABASE_URL: str = "postgresql+psycopg2://user:password@host:port/dbname"

    class Config:
        # .env 파일 우선순위로 설정 로드 (python-dotenv 설치 시)
        # env_file = ".env"
        # env_file_encoding = 'utf-8'
        pass # .env 안 쓰면 pass

settings = Settings()

# 사용 예시: 다른 파일에서 from app.core.config import settings 후 settings.BIMS_API_KEY 로 사용