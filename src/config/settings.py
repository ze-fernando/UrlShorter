from dotenv import load_dotenv 
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    DATABASE: str


settings = Settings()