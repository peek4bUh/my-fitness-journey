from flask_restx import fields
from typing import List

from api.core.namespaces import programs_ns
from ..program_section.program_section_input import ProgramSectionInput


class ProgramInput:
    """Input Object for Program data."""

    schema = programs_ns.model('ProgramInput', {
        'title': fields.String(required=True, description='Program title', example='6-Week Beginner Strength Program'),
        'description': fields.String(required=True, description='Program description', example='A 6-week plan focusing on full-body strength.'),
        'duration_weeks': fields.Integer(required=True, description='Duration in weeks', example=6),
        'sections': fields.List(fields.Nested(ProgramSectionInput().schema), required=True, description='Workout sections')
    })

    def __init__(
            self,
            title: str = None,
            description: str = None,
            duration_weeks: int = None,
            sections: List[ProgramSectionInput] = None):
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
