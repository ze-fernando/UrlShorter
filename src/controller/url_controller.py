from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.url_schema import UrlRequest 
from src.service.url_service import UrlService
from src.database.connection import get_db


router = APIRouter()


@router.get('/')
def get_all(db: Session = Depends(get_db)):
    service = UrlService(db)
    all_urls = service.get_all()
    return all_urls

@router.get('/{code}')
def get_by_code(code: str, db: Session = Depends(get_db)):
    service = UrlService(db)
    url = service.get_by_short_code(code)

    return url 

@router.post('/')
async def create_url(request: UrlRequest, db: Session = Depends(get_db)):
    service = UrlService(db)
    response = service.create(url=request.url)
    return response 