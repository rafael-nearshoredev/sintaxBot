from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Syntax Analyzer"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"
    DEFAULT_LANGUAGE: str = "es"
    
    class Config:
        env_file = ".env"

settings = Settings()
