import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    api_key: str = Field(..., alias="FASTAPI_API_KEY") 
    # jwt_secret: str = os.getenv("JWT_SECRET", "your_jwt_secret")
    # database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache
def get_settings():
    return Settings()
