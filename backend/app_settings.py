import os
from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY") 
PORTIA_API_KEY=os.getenv("PORTIA_API_KEY")
NEWSAPI_KEY=os.getenv("NEWSAPI_KEY")

class Settings(BaseSettings):
    PORT: int = 8000
    GOOGLE_API_KEY: Optional[str] = GOOGLE_API_KEY
    TAVILY_API_KEY: Optional[str] = TAVILY_API_KEY
    PORTIA_API_KEY: Optional[str] = PORTIA_API_KEY
    PORTIA_LLM_PROVIDER: Optional[str] = "google"
    NEWSAPI_KEY: Optional[str] = NEWSAPI_KEY

settings = Settings()