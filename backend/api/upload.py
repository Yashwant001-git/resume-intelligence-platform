from utils.logger import logger

from fastapi import APIRouter, UploadFile, File

from services.upload_service import UploadService

router = APIRouter()


@router.post("/")
async def upload_resume(
    file: UploadFile = File(...)
):
    """
    Upload a resume to the system.
    """

    response = await UploadService.upload_resume(file)

    return response