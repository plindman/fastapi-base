from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

from .config import get_settings
settings = get_settings()

# Security schemes
api_key_scheme = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Security(api_key_scheme)):
    # Verify API key
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return True
