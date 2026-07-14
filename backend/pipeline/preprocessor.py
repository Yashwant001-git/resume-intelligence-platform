import re

from pipeline.context import ResumeContext
from utils.logger import logger


class Preprocessor:
    """
    Cleans and normalizes extracted resume text.
    """

    @classmethod
    def clean(cls, context: ResumeContext) -> None:
        """
        Main preprocessing pipeline.
        """

        logger.info("Starting text preprocessing.")

        text = context.raw_text

        text = cls._normalize_newlines(text)
        text = cls._remove_non_printable(text)
        text = cls._remove_extra_spaces(text)
        text = cls._remove_blank_lines(text)
        text = cls._trim_lines(text)

        context.clean_text = text

        logger.info("Text preprocessing completed.")

    @staticmethod
    def _normalize_newlines(text: str) -> str:
        """
        Convert Windows and old Mac newlines to Unix style.
        """
        return text.replace("\r\n", "\n").replace("\r", "\n")

    # @staticmethod
    # def _remove_non_printable(text: str) -> str:
    #     """
    #     Remove invisible/non-printable characters.
    #     """
    #     return re.sub(r"[\x00-\x1F\x7F-\x9F]", "", text)

    @staticmethod
    def _remove_non_printable(text: str) -> str:
        """
        Remove non-printable characters except newline and tab.
        """

        cleaned = []

        for ch in text:
            if ch.isprintable() or ch in ("\n", "\t"):
                cleaned.append(ch)

        return "".join(cleaned)

    @staticmethod
    def _remove_extra_spaces(text: str) -> str:
        """
        Replace multiple spaces or tabs with a single space.
        """
        return re.sub(r"[ \t]+", " ", text)

    @staticmethod
    def _remove_blank_lines(text: str) -> str:
        """
        Collapse multiple blank lines into a single blank line.
        """
        return re.sub(r"\n{3,}", "\n\n", text)

    @staticmethod
    def _trim_lines(text: str) -> str:
        """
        Strip whitespace from each line.
        """
        lines = [line.strip() for line in text.split("\n")]
        return "\n".join(lines).strip()