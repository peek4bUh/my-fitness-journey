from dataclasses import dataclass
from flask_restx import fields
from typing import List

from api.core.namespaces import programs_ns
from .program_section import ProgramSectionInput


@dataclass
class ProgramInput:
    """Input Object for Program data."""

    title: str = None
    description: str = None
    duration_weeks: int = None
    sections: List[ProgramSectionInput] = None

    schema = programs_ns.model('ProgramInput', {
        'title': fields.String(required=True, description='Program title', example='6-Week Beginner Strength Program'),
        'description': fields.String(required=True, description='Program description', example='A 6-week plan focusing on full-body strength.'),
        'duration_weeks': fields.Integer(required=True, description='Duration in weeks', example=6),
        'sections': fields.List(fields.Nested(ProgramSectionInput().schema), required=True, description='Workout sections')
    })


@dataclass
class ProgramOutput:
    """Output Object for Program data."""

    id: str
    title: str
    description: str
    duration_weeks: int
    sections: List[ProgramSectionInput]
