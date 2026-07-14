import fitz  # PyMuPDF
from pathlib import Path

from utils.logger import logger


class PDFParser:
    """
    Handles text extraction from PDF files.
    """

    @staticmethod
    def extract_text(file_path: Path) -> str:
        """
        Extract all text from a PDF.

        Args:
            file_path (Path): Path to the PDF file.

        Returns:
            str: Extracted text.
        """

        logger.info(f"Starting PDF parsing: {file_path.name}")

        try:
            document = fitz.open(file_path)
            extracted_text = []

            for page_number, page in enumerate(document, start=1):

                logger.info(f"Extracting Page {page_number}")
                text = page.get_text()
                extracted_text.append(text)

            document.close()

            final_text = "\n".join(extracted_text)

            logger.info(
                f"Successfully extracted {len(final_text)} characters."
            )

            return final_text

        except Exception as e:

            logger.error(f"PDF Parsing Failed : {e}")
            raise Exception("Unable to parse PDF.")