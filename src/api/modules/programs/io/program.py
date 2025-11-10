from typing import List

from .program_section import ProgramSectionDto


class ProgramDto:
    """Data Transfer Object for Program data."""

    def __init__(
            self,
            title: str,
            description: str,
            duration_weeks: int,
            sections: List[ProgramSectionDto]):
        self.title = title
        self.description = description
        self.duration_weeks = duration_weeks
        self.sections = sections
