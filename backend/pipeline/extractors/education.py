import re

from config.degrees import DEGREES
from pipeline.context import ResumeContext
from pipeline.entities import Education
from utils.logger import logger


class EducationExtractor:
    """
    Extract education information from the resume.
    """

    @classmethod
    def process(cls, context: ResumeContext) -> None:

        logger.info("Starting Education Extraction.")

        text = context.sections.education

        if not text.strip():
            logger.info("No education section found.")
            return

        education = cls._extract(text)

        context.candidate.education = education

        logger.info(
            f"Extracted {len(education)} education record(s)."
        )

    @classmethod
    def _extract(cls, text: str) -> list[Education]:

        record = Education()

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        for line in lines:

            degree = cls._extract_degree(line)
            duration = cls._extract_duration(line)
            cgpa = cls._extract_cgpa(line)
            institute = cls._extract_institute(
                line,
                degree,
                duration,
                cgpa,
            )

            if degree and not record.degree:
                record.degree = degree

            if duration and not record.duration:
                record.duration = duration

            if cgpa and not record.cgpa:
                record.cgpa = cgpa

            if institute and not record.institute:
                record.institute = institute

        return [record]

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    @staticmethod
    def _normalize(text: str) -> str:

        return (
            text.lower()
            .replace(".", "")
            .replace("(", "")
            .replace(")", "")
            .replace("-", " ")
        )

    # --------------------------------------------------
    # Degree
    # --------------------------------------------------

    @classmethod
    def _extract_degree(cls, line: str) -> str:

        normalized = cls._normalize(line)

        for degree in DEGREES:

            if cls._normalize(degree) in normalized:

                # Stop before separators like —, | or year
                split_pattern = (
                    r"\s+(?:—|-|\|)\s+|\b(?:19|20)\d{2}\b"
                )

                degree_part = re.split(
                    split_pattern,
                    line,
                    maxsplit=1
                )[0]

                return degree_part.strip()

        return ""

    # --------------------------------------------------
    # Duration
    # --------------------------------------------------

    @staticmethod
    def _extract_duration(line: str) -> str:

        pattern = (
            r"(19|20)\d{2}\s*[-–]\s*((19|20)\d{2}|Present)"
        )

        match = re.search(
            pattern,
            line,
            re.IGNORECASE,
        )

        return match.group(0) if match else ""

    # --------------------------------------------------
    # CGPA / GPA
    # --------------------------------------------------

    @staticmethod
    def _extract_cgpa(line: str) -> str:

        pattern = (
            r"(?:cgpa|gpa)\s*[:\-]?\s*(\d+(?:\.\d+)?)"
        )

        match = re.search(
            pattern,
            line,
            re.IGNORECASE,
        )

        return match.group(1) if match else ""

    # --------------------------------------------------
    # Institute
    # --------------------------------------------------

    @staticmethod
    def _extract_institute(
        line: str,
        degree: str,
        duration: str,
        cgpa: str,
    ) -> str:

        if degree:
            line = line.replace(degree, "")

        if duration:
            line = line.replace(duration, "")

        line = re.sub(
            r"(?:cgpa|gpa)\s*[:\-]?\s*\d+(\.\d+)?(\s*/\s*10)?",
            "",
            line,
            flags=re.IGNORECASE,
        )

        # Remove separators
        line = re.sub(r"[|]", " ", line)
        line = re.sub(r"[—-]", " ", line)

        # Remove multiple spaces
        line = " ".join(line.split())

        return line.strip(", ")