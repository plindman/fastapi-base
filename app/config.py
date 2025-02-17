import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    # jwt_secret: str = os.getenv("JWT_SECRET", "your_jwt_secret")
    # database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    class Config:
        env_file = ".env"

settings = Settings()