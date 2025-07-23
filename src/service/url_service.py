from src.database.connection import get_db
from sqlalchemy.orm import Session
from src.models.url import Url

class UrlService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self):
        return self.db.query(Url).all()

    def get_by_short_code(self, code: str):
        return self.db.query(Url).filter(Url.short_code == code).all()

    def create(self, url: str):
        url = url(original_url=url)
        url.generate_short_code()
        self.db.add(url)
        self.db.commit()
        self.db.refresh(url)
        return url