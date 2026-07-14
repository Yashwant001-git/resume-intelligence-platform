import json
from pathlib import Path


class SkillLoader:
    """
    Loads all supported technical skills from the configuration file.
    """

    _skills = None

    @classmethod
    def load_skills(cls) -> set[str]:

        if cls._skills is not None:
            return cls._skills

        config_path = (
            Path(__file__).parent.parent
            / "config"
            / "skills.json"
        )

        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        skills = set()

        for category in data.values():
            skills.update(skill.lower() for skill in category)

        cls._skills = skills

        return cls._skills