import re

from pipeline.context import ResumeContext
from utils.logger import logger
from utils.patterns import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN,
    URL_PATTERN,
)


class PersonalInfoExtractor:
    """
    Extract personal information from the resume.
    """

    IGNORE_LINES = {
        "resume",
        "curriculum vitae",
        "cv",
    }

    @classmethod
    def process(cls, context: ResumeContext) -> None:
        """
        Populate candidate.personal_info from the
        personal_information section.
        """

        logger.info("Starting Personal Information Extraction.")

        text = context.sections.personal_information

        info = context.candidate.personal_info

        info.name = cls._extract_name(text)
        info.email = cls._extract_email(text)
        info.phone = cls._extract_phone(text)

        social_info = context.candidate.social_links

        social_info.linkedin = cls._extract_linkedin(text)
        social_info.github = cls._extract_github(text)
        social_info.portfolio = cls._extract_portfolio(text)

        logger.info("Personal Information Extraction Completed.")

    # --------------------------------------------------
    # Name
    # --------------------------------------------------

    @classmethod
    def _extract_name(cls, text: str) -> str:

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        for line in lines[:10]:

            lower = line.lower()

            if lower in cls.IGNORE_LINES:
                continue

            if re.search(EMAIL_PATTERN, line):
                continue

            if re.search(PHONE_PATTERN, line):
                continue

            if "linkedin" in lower:
                continue

            if "github" in lower:
                continue

            if re.search(URL_PATTERN, line):
                continue

            words = line.split()

            if not (2 <= len(words) <= 4):
                continue

            if all(
                word.replace(".", "").replace("-", "").isalpha()
                for word in words
            ):
                return line

        return ""

    # --------------------------------------------------
    # Email
    # --------------------------------------------------

    @staticmethod
    def _extract_email(text: str) -> str:

        match = re.search(EMAIL_PATTERN, text)

        return match.group(0) if match else ""

    # --------------------------------------------------
    # Phone
    # --------------------------------------------------

    @staticmethod
    def _extract_phone(text: str) -> str:

        match = re.search(PHONE_PATTERN, text)

        return match.group(0).strip() if match else ""

    # --------------------------------------------------
    # LinkedIn
    # --------------------------------------------------

    @staticmethod
    def _extract_linkedin(text: str) -> str:

        match = re.search(
            LINKEDIN_PATTERN,
            text,
            re.IGNORECASE,
        )

        return match.group(0) if match else ""

    # --------------------------------------------------
    # GitHub
    # --------------------------------------------------

    @staticmethod
    def _extract_github(text: str) -> str:

        match = re.search(
            GITHUB_PATTERN,
            text,
            re.IGNORECASE,
        )

        return match.group(0) if match else ""

    # --------------------------------------------------
    # Portfolio
    # --------------------------------------------------

    @staticmethod
    def _extract_portfolio(text: str) -> str:

        urls = re.findall(URL_PATTERN, text)

        for url in urls:

            lower = url.lower()

            if "linkedin" in lower:
                continue

            if "github" in lower:
                continue

            return url

        return ""