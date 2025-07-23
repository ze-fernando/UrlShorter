from sqlalchemy import Column, Integer, String
from src.database.connection import Base
import string, random

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True)

    def generate_short_code(self, length=6):
        self.short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))