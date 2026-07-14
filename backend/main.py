from utils.logger import logger

from fastapi import FastAPI

from api.health import router as health_router
from api.upload import router as upload_router


app = FastAPI(
    title='Resume Intelligence Platform',
    version='1.0.0'
)

app.include_router(
    health_router,
    prefix='/health',
    tags=['Health']
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)

logger.info("Backend started successfully.")