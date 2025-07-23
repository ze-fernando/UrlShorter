from pydantic import BaseModel
from datetime import datetime

class UrlRequest(BaseModel):
    url: str


class ShortCodeRequest(BaseModel):
    short_code: str