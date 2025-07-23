from fastapi import FastAPI
from src.controller.url_controller import router
from src.config.settings import settings
from src.database.connection import Base, engine

from src.models.url import Url

app = FastAPI(title=settings.APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(router)

