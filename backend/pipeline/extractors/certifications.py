from pipeline.context import ResumeContext
from utils.logger import logger


class CertificationExtractor:
    """
    Extract certifications from the resume.
    """

    @classmethod
    def process(cls, context: ResumeContext) -> None:

        logger.info("Starting Certification Extraction.")

        text = context.sections.certifications

        if not text.strip():
            logger.info("No certification section found.")
            return

        certifications = []

        for line in text.split("\n"):

            line = (
                line.strip()
                .lstrip("•")
                .lstrip("-")
                .strip()
            )

            if line:
                certifications.append(line)

        context.candidate.certifications = certifications

        logger.info(
            f"Extracted {len(certifications)} certification(s)."
        )