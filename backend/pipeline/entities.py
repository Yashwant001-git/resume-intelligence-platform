from dataclasses import dataclass
from dataclasses import field


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


#Education
@dataclass
class Education:

    degree: str = ""

    institute: str = ""

    duration: str = ""

    cgpa: str = ""


#Experince
@dataclass
class Experience:

    company: str = ""

    designation: str = ""

    duration: str = ""

    description: str = ""


#project
@dataclass
class Project:

    title: str = ""

    description: str = ""

    technologies: list[str] = field(default_factory=list)

#Social media links
@dataclass
class SocialLinks:
    linkedin: str = ""
    github: str = ""
    portfolio: str = ""

#Perssonal info
@dataclass
class PersonalInfo:
    name: str = ""
    email: str = ""
    phone: str = ""



@dataclass
class Candidate:


    # summary: str = ""
    personal_info: PersonalInfo = field(default_factory=PersonalInfo)

    social_links: SocialLinks = field(default_factory=SocialLinks)

    skills: list[str] = field(default_factory=list)

    education: list[Education] = field(default_factory=list)

    experience: list[Experience] = field(default_factory=list)

    projects: list[Project] = field(default_factory=list)

    certifications: list[str] = field(default_factory=list)

    languages: list[str] = field(default_factory=list) 