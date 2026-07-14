from utils.logger import logger

from pipeline.context import ResumeContext
from pipeline.pdf_parser import PDFParser


class ParserManager:
    """
    Selects the appropriate parser based on the resume file type.
    """

    @staticmethod
    def parse(context: ResumeContext) -> None:
        """
        Parse the uploaded resume and populate the ResumeContext.

        Args:
            context (ResumeContext): Shared pipeline context.
        """

        file_path = context.file_path
        extension = file_path.suffix.lower()

        logger.info(f"Selecting parser for '{extension}'")

        if extension == ".pdf":
            context.raw_text = PDFParser.extract_text(file_path)
            return

        raise ValueError(
            f"No parser available for '{extension}' files."
        )