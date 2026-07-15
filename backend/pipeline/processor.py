from pathlib import Path

from pipeline.context import ResumeContext
from pipeline.parser_manager import ParserManager
from pipeline.preprocessor import Preprocessor
from pipeline.section_detector import SectionDetector
from utils.logger import logger

from pipeline.extractors.personal_info import PersonalInfoExtractor
from pipeline.extractors.skills import SkillsExtractor
from pipeline.extractors.education import EducationExtractor
from pipeline.extractors.experience import ExperienceExtractor
from pipeline.extractors.projects import ProjectExtractor
from pipeline.extractors.certifications import CertificationExtractor

class ResumeProcessor:
    """
    Orchestrates the complete resume processing pipeline.
    """

    @staticmethod
    def process(file_path: Path) -> ResumeContext:
        """
        Execute the complete resume processing pipeline.

        Args:
            file_path (Path): Path to the uploaded resume.

        Returns:
            ResumeContext: Contains all processed data.
        """

        logger.info("=" * 80)
        logger.info("Starting Resume Processing Pipeline")
        logger.info("=" * 80)

        # Initialize pipeline context
        context = ResumeContext(file_path=file_path)

        # Stage 1 : Parse Resume
        ParserManager.parse(context)
        logger.info("Resume parsing completed.")

        # Stage 2 : Preprocess Text
        Preprocessor.clean(context)
        logger.info("Text preprocessing completed.")

        # Stage 3 : Detect Sections
        SectionDetector.detect(context)
        logger.info("Section detection completed.")

        # Stage 4.1 : Personal Info Extraction
        PersonalInfoExtractor.process(context)
        logger.info("Personal information extraction completed.")

        # Stage 4.2 : Skill Extraction
        SkillsExtractor.process(context)
        logger.info("Skill extraction completed.")

        # Stage 4.3 : Eduction Extraction
        EducationExtractor.process(context)
        logger.info("Education extraction completed.")

        #Stage 4.4 : Experience Extraction
        ExperienceExtractor.process(context)
        logger.info("Experience extraction completed.")

        #Stage 4.5 : Project Extractor
        ProjectExtractor.process(context)
        logger.info("Project extraction completed.")

        #Stage 4.6 : Certificates Extractor
        CertificationExtractor.process(context)
        logger.info("Certification extraction completed.")

        logger.info("=" * 80)
        logger.info("Resume Processing Pipeline Completed")
        logger.info("=" * 80)

        return context