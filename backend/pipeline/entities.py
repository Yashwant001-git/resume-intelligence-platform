from dataclasses import dataclass


@dataclass
class ResumeSections:
    """
    Stores all detected resume sections.
    """

    personal_information: str = ""

    summary: str = ""

    skills: str = ""

    experience: str = ""

    education: str = ""

    projects: str = ""

    certifications: str = ""

    languages: str = ""

    achievements: str = ""

    interests: str = ""