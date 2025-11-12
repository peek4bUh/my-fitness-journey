from typing import List

from .program_section import ProgramSectionDto


class ProgramDto:
    """Data Transfer Object for Program data."""

    def __init__(
            self,
            title: str = None,
            description: str = None,
            duration_weeks: int = None,
            sections: List[ProgramSectionDto] = None):
        self.title = title
        self.description = description
        self.duration_weeks = duration_weeks
        self.sections = sections

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_duration_weeks(self):
        return self.duration_weeks

    def set_duration_weeks(self, duration_weeks):
        self.duration_weeks = duration_weeks

    def get_sections(self):
        return self.sections

    def set_sections(self, sections):
        self.sections = sections

    def __repr__(self) -> str:
        title = repr(self.title)
        desc = repr(self.description)
        weeks = repr(self.duration_weeks)
        # show number of sections instead of full nested dump
        sections_info = (
            f"{len(self.sections)} section(s)" if self.sections is not None else "None"
        )
        return f"ProgramDto(title={title}, description={desc}, duration_weeks={weeks}, sections={sections_info})"


class ProgramOutput:
    """Output Object for Program data."""

    def __init__(
            self,
            id: int = None,
            title: str = None,
            description: str = None,
            duration_weeks: int = None,
            sections: List[ProgramSectionDto] = None):
        self.id = id
        self.title = title
        self.description = description
        self.duration_weeks = duration_weeks
        self.sections = sections

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_duration_weeks(self):
        return self.duration_weeks

    def set_duration_weeks(self, duration_weeks):
        self.duration_weeks = duration_weeks

    def get_sections(self):
        return self.sections

    def set_sections(self, sections):
        self.sections = sections
