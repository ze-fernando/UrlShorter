from fastapi import FastAPI
from src.controller.url_controller import router
from src.config.settings import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

