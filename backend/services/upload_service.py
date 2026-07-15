from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

from config.settings import SUPPORTED_FORMATS, MAX_FILE_SIZE, UPLOAD_DIR
from utils.logger import logger
from pipeline.processor import ResumeProcessor
from exporters.excel_exporter import ExcelExporter

class UploadService:

    @staticmethod
    async def upload_resume(file: UploadFile) -> dict:
        """
        Validate and save uploaded resume.
        """

        logger.info("Upload request received.")

        # Validate Extension
        extension = Path(file.filename).suffix.lower()

        if extension not in SUPPORTED_FORMATS:
            logger.warning(f"Unsupported file type: {extension}")

            raise HTTPException(
                status_code=400,
                detail="Unsupported file format."
            )

        # Read File
        contents = await file.read()

        # Empty file
        if len(contents) == 0:

            logger.warning("Uploaded file is empty.")

            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        # File too large
        if len(contents) > MAX_FILE_SIZE:

            logger.warning("Uploaded file exceeds maximum size.")

            raise HTTPException(
                status_code=400,
                detail="File exceeds maximum size."
            )

        # Generate Unique Filename
        file_id = str(uuid4())

        filename = f"{file_id}{extension}"

        save_path = UPLOAD_DIR / filename

        # Save File
        with open(save_path, "wb") as f:
            f.write(contents)

        logger.info(f"Resume saved successfully: {filename}")

        # Parse Resume
        # text = ResumeProcessor.process(save_path)
        context = ResumeProcessor.process(save_path)

        #Export Info to Excel
        ExcelExporter.export(context.candidate)

        logger.info("Resume parsed successfully.")
        
        # Response
        return {

            "message": "Resume uploaded successfully.",

            "file_id": file_id,

            "filename": filename,

            "original_filename": file.filename,

            "size": len(contents)
        }
    