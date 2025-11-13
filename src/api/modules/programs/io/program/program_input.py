from flask_restx import fields

from api.core.namespaces import programs_ns
from api.modules.programs.io.program_section.program_section_input import ProgramSectionInput


class ProgramInput:
    """Input Object for Program data."""

    schema = programs_ns.model('ProgramInput', {
        'title': fields.String(required=True, description='Program title', example='6-Week Beginner Strength Program'),
        'description': fields.String(required=True, description='Program description', example='A 6-week plan focusing on full-body strength.'),
        'duration_weeks': fields.Integer(required=True, description='Duration in weeks', example=6),
        'sections': fields.List(fields.Nested(ProgramSectionInput().schema), required=True, description='Workout sections')
    })
