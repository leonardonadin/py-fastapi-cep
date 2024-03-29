from fastapi import FastAPI

from app.routers import zipcode
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(zipcode.router)