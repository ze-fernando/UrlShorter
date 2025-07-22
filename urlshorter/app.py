from fastapi import FastAPI
from urlshorter.controller.url_controller import router
from urlshorter.config.settings import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

