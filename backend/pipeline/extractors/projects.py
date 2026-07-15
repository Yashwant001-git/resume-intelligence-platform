# import re

# from pipeline.context import ResumeContext
# from pipeline.entities import Project
# from utils.logger import logger
# from utils.skill_loader import SkillLoader


# class ProjectExtractor:
#     """
#     Extract projects from the resume.
#     """

#     @classmethod
#     def process(cls, context: ResumeContext) -> None:

#         logger.info("Starting Project Extraction.")

#         text = context.sections.projects

#         if not text.strip():
#             logger.info("No project section found.")
#             return

#         projects = cls._extract(text)

#         context.candidate.projects = projects

#         logger.info(
#             f"Extracted {len(projects)} project(s)."
#         )

#     @classmethod
#     def _extract(cls, text: str) -> list[Project]:

#         lines = [
#             line.strip()
#             for line in text.split("\n")
#             if line.strip()
#         ]

#         if not lines:
#             return []

#         project = Project()

#         project.title = lines[0]

#         project.technologies = cls._extract_skills(text)

#         if len(lines) > 1:
#             project.description = "\n".join(lines[1:])

#         return [project]

#     @staticmethod
#     def _extract_skills(text: str) -> list[str]:

#         skills_db = SkillLoader.load_skills()

#         tokens = re.split(r"[,\n|;/•()]+", text)

#         skills = []

#         for token in tokens:

#             token = token.strip()

#             if token.lower() in skills_db:
#                 skills.append(token)

#         return list(dict.fromkeys(skills))





import re

from pipeline.context import ResumeContext
from pipeline.entities import Project
from utils.logger import logger
from utils.skill_loader import SkillLoader


class ProjectExtractor:
    """
    Extract projects from the resume.
    """

    @classmethod
    def process(cls, context: ResumeContext) -> None:

        logger.info("Starting Project Extraction.")

        text = context.sections.projects

        if not text.strip():
            logger.info("No project section found.")
            return

        context.candidate.projects = cls._extract(text)

        logger.info(
            f"Extracted {len(context.candidate.projects)} project(s)."
        )

    @classmethod
    def _extract(cls, text: str) -> list[Project]:

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        projects = []

        current_project = None
        description = []

        for line in lines:

            # ----------------------------
            # New Project Starts
            # ----------------------------

            if cls._is_project_title(line):

                # Save previous project
                if current_project:

                    current_project.description = "\n".join(description).strip()

                    projects.append(current_project)

                current_project = Project()

                current_project.title = line

                description = []

                continue

            if current_project is None:
                continue

            # ----------------------------
            # Technologies
            # ----------------------------

            if line.lower().startswith("technologies"):

                current_project.technologies = cls._extract_skills(line)

                continue

            # ----------------------------
            # Description
            # ----------------------------

            description.append(line)

        # Save last project

        if current_project:

            current_project.description = "\n".join(description).strip()

            projects.append(current_project)

        return projects

    # ==================================================
    # Project Title Detector
    # ==================================================

    @staticmethod
    def _is_project_title(line: str) -> bool:

        line = line.strip()

        if not line:
            return False

        if line.startswith("•"):
            return False

        if line.lower().startswith("technologies"):
            return False

        # Ignore very short lines
        if len(line) < 10:
            return False

        # Your resume titles contain "|"
        if "|" in line:
            return True

        return False

    # ==================================================
    # Skill Extraction
    # ==================================================

    @staticmethod
    def _extract_skills(text: str) -> list[str]:

        skill_db = SkillLoader.load_skills()

        tokens = re.split(r"[,\n|;/•()]+", text)

        skills = []

        for token in tokens:

            token = token.strip()

            if token.lower() in skill_db:
                skills.append(token)

        return list(dict.fromkeys(skills))