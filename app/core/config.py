from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import List, Optional
import secrets

class Settings(BaseSettings):
    PROJECT_NAME: str = "Todo API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
    # Backend CORS origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [item.strip() for item in v.split(",")]
        return v
    
    # Database
    DATABASE_URL: str = "sqlite:///./todos.db"
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()