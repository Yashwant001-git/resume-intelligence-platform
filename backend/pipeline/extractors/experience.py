import re

from config.designations import DESIGNATIONS
from pipeline.context import ResumeContext
from pipeline.entities import Experience
from utils.logger import logger


class ExperienceExtractor:
    """
    Extract work experience from the resume.
    """

    @classmethod
    def process(cls, context: ResumeContext) -> None:

        logger.info("Starting Experience Extraction.")

        text = context.sections.experience

        if not text.strip():
            logger.info("No experience section found.")
            return

        experiences = cls._extract(text)

        context.candidate.experience = experiences

        logger.info(
            f"Extracted {len(experiences)} experience record(s)."
        )

    @classmethod
    def _extract(cls, text: str) -> list[Experience]:

        experience = Experience()

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        description = []

        for line in lines:

            # -------------------------------
            # Header
            # -------------------------------

            if not experience.designation:

                designation, company = cls._extract_header(line)

                if designation:

                    experience.designation = designation
                    experience.company = company

                    continue

            # -------------------------------
            # Duration
            # -------------------------------

            duration = cls._extract_duration(line)

            if duration and not experience.duration:

                experience.duration = duration

                continue

            # -------------------------------
            # Description
            # -------------------------------

            description.append(line)

        experience.description = "\n".join(description)

        return [experience]

    # ============================================================
    # Helpers
    # ============================================================

    @staticmethod
    def _normalize(text: str) -> str:

        return (
            text.lower()
            .replace(".", "")
            .replace("-", " ")
        )

    # ============================================================
    # Header
    # ============================================================

    @classmethod
    def _extract_header(cls, line: str) -> tuple[str, str]:

        separators = [
            "—",
            "-",
            "|",
        ]

        for separator in separators:

            if separator not in line:
                continue

            left, right = line.split(separator, 1)

            left = left.strip()
            right = right.strip()

            for designation in DESIGNATIONS:

                if cls._normalize(designation) in cls._normalize(left):

                    return left, right

        return "", ""

    # ============================================================
    # Duration
    # ============================================================

    @staticmethod
    def _extract_duration(line: str) -> str:

        pattern = (
            r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|"
            r"Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|"
            r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
            r"\s+\d{4}"
            r"(\s*[-–]\s*"
            r"("
            r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|"
            r"Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|"
            r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
            r"\s+\d{4}"
            r"|Present"
            r"))?"
        )

        match = re.search(
            pattern,
            line,
            re.IGNORECASE,
        )

        return match.group(0) if match else ""