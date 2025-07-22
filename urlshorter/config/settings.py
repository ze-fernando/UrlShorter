from python_dotenv import load_dotenv
from pydantic_settings import BaseModel

load_dotenv()

class Settings(BaseModel):
    DATABASE: str


settings = Settings()