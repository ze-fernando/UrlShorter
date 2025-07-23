from pydantic import BaseModel
from datetime import datetime

class UrlRequest(BaseModel):
    url: str


class UrlResponse(BaseModel):
    id: int
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime
