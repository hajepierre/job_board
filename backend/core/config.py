import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    PROJECT_TITLE: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    # DATABASE CONFIGURATIONS
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', '5432')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URL=f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()