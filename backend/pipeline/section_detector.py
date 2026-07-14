# # Find Skills, Education, Experience sections.
# from config.section_headers import SECTION_HEADERS
# from pipeline.entities import ResumeSections
# from pipeline.context import ResumeContext
# import re


# class SectionDetector:
#     """
#     Detects resume section headings.
#     """

#     @staticmethod
#     def _normalize_heading(text: str) -> str:
#         """
#         Normalize a heading before comparison.

#         Example:
#             " TECHNICAL Skills : " -> "technical skills"
#         """

#         text = text.strip().lower()

#         # Remove trailing punctuation
#         text = re.sub(r"[:\-]+$", "", text)

#         # Collapse multiple spaces
#         text = re.sub(r"\s+", " ", text)

#         return text

#     @classmethod
#     def is_heading(cls, line: str) -> tuple[bool, str | None]:
#         """
#         Checks whether a line is a resume heading.

#         Returns:
#             (True, section_name)
#             (False, None)
#         """

#         normalized = cls._normalize_heading(line)

#         for section, headings in SECTION_HEADERS.items():

#             if normalized in headings:
#                 return True, section

#         return False, None
    
#     @classmethod
#     def detect(cls, context: ResumeContext) -> None:
#         """
#         Detect resume sections and populate ResumeContext.
#         """

#         lines = context.clean_text.split("\n")

#         current_section = "personal_information"

#         section_data = {
#             field: []
#             for field in ResumeSections().__dict__.keys()
#         }

#         for line in lines:

#             line = line.strip()

#             if not line:
#                 continue

#             is_heading, section = cls.is_heading(line)

#             if is_heading:

#                 current_section = section

#                 continue

#             section_data[current_section].append(line)

#         context.sections = ResumeSections(
#             **{
#                 key: "\n".join(value)
#                 for key, value in section_data.items()
#             }
#         )





import re

from config.section_headers import SECTION_HEADERS
from pipeline.context import ResumeContext
from pipeline.entities import ResumeSections
from utils.logger import logger
from dataclasses import asdict


class SectionDetector:
    """
    Detects resume section headings and stores the extracted
    section content in ResumeContext.
    """

    @staticmethod
    def _normalize_heading(text: str) -> str:
        """
        Normalize a heading before comparison.

        Example:
            " TECHNICAL Skills : " -> "technical skills"
        """

        text = text.strip().lower()

        # Remove trailing punctuation
        text = re.sub(r"[:\-]+$", "", text)

        # Collapse multiple spaces
        text = re.sub(r"\s+", " ", text)

        return text

    @classmethod
    def is_heading(cls, line: str) -> tuple[bool, str | None]:
        """
        Checks whether a line is a resume heading.

        Returns:
            (True, section_name)
            (False, None)
        """

        normalized = cls._normalize_heading(line)

        for section, headings in SECTION_HEADERS.items():
            if normalized in headings:
                logger.debug(
                    f"Heading detected: '{line}' -> '{section}'"
                )
                return True, section

        return False, None

    @classmethod
    def detect(cls, context: ResumeContext) -> None:
        """
        Detect resume sections and populate ResumeContext.
        """

        logger.info("=" * 60)
        logger.info("Starting Section Detection")
        logger.info("=" * 60)

        if not context.clean_text:
            logger.warning("No cleaned text found in ResumeContext.")
            return

        lines = context.clean_text.split("\n")

        logger.info(f"Total lines to process: {len(lines)}")

        current_section = "personal_information"

        section_data = {
            field: []
            for field in ResumeSections().__dict__.keys()
        }

        logger.info("Initialized section storage.")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            is_heading, section = cls.is_heading(line)

            if is_heading:

                logger.info(f"Heading detected: '{line}' --> Section: '{section}'")

                current_section = section

                continue

            section_data[current_section].append(line)

        logger.info("Finished scanning all lines.")

        context.sections = ResumeSections(
            **{
                key: "\n".join(value)
                for key, value in section_data.items()
            }
        )

        logger.info("ResumeSections object created successfully.")