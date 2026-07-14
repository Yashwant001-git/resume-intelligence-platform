from dataclasses import dataclass, field
from pathlib import Path

from pipeline.entities import ResumeSections


@dataclass
class ResumeContext:

    file_path: Path

    raw_text: str = ""

    clean_text: str = ""

    sections: ResumeSections = field(
        default_factory=ResumeSections
    )

    extracted_data: dict = field(default_factory=dict)

    validated_data: dict = field(default_factory=dict)