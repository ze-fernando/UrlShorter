from fastapi import FastAPI
from src.controller.url_controller import router
from src.config.settings import settings

app = FastAPI(title=settings.APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(router)

