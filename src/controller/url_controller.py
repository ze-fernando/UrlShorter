from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def hello():
    return {'mesage': 'hello world'}
