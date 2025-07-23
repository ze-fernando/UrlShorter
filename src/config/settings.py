from dotenv import load_dotenv 
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE: str
    APP_NAME: str


settings = Settings()