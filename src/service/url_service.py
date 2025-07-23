from src.database.connection import get_db
from src.models.url import Url

class UrlService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all():
        return self.db.query(Url).all()

    def create(url: string):
        url = Url(url)
        url.generate_short_code()
        self.db.add(url)
        self.db.commit()