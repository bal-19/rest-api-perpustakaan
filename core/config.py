import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Unofficial Perpusnas Rest API"
    MONGO_URL: str = os.getenv("MONGO_URL")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

    class Config:
        env_file = ".env"

settings = Settings()
