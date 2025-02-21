from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    api_key: str = Field(..., alias="FASTAPI_API_KEY") 

    model_config = SettingsConfigDict(env_file=".env", 
                                      env_file_encoding="utf-8",
                                      extra="allow")

@lru_cache
def get_settings():
    return Settings()
