from flask_restx import fields

from api.core.namespaces import programs_ns
from api.modules.programs.io.program_exercise.program_exercise_input import ProgramExerciseInput


class ProgramSectionInput:
    """Input Object for Program Section data."""

    schema = programs_ns.model('ProgramSection', {
        'name': fields.String(required=True, description='Section name (e.g., Day 1 - Upper Body)', example='Day 1 - Upper Body'),
        'exercises': fields.List(fields.Nested(ProgramExerciseInput().schema), required=True, description='List of exercises')
    })
