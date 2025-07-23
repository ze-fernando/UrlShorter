from fastapi import APIRouter
from src.schemas.url import UrlRequest, UrlResponse

router = APIRouter()


@router.get('/')
def hello():
    return {'mesage': 'hello world'}

@router.post('/', response_model=UrlResponse)
def create_url(request: UrlRequest):
    ...