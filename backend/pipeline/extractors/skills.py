import re

from pipeline.context import ResumeContext
from utils.logger import logger
from utils.skill_loader import SkillLoader


class SkillsExtractor:
    """
    Extract technical skills from the resume.
    """

    @classmethod
    def process(cls, context: ResumeContext) -> None:

        logger.info("Starting Skills Extraction.")

        text = context.sections.skills

        context.candidate.skills = cls._extract(text)

        logger.info(
            f"Extracted {len(context.candidate.skills)} skills."
        )

    @staticmethod
    def _extract(text: str) -> list[str]:

        skill_db = SkillLoader.load_skills()

        # Split using common separators
        tokens = re.split(r"[,;\n|•/]+", text)

        extracted = []

        for token in tokens:

            token = token.strip()

            if not token:
                continue

            if token.lower() in skill_db:
                extracted.append(token)

        # Remove duplicates while preserving order
        return list(dict.fromkeys(extracted))