from dataclasses import dataclass
from flask_restx import fields

from api.core.namespaces import programs_ns


@dataclass
class ProgramExerciseInput:
    """Input Object for Program Exercise data."""

    name: str = None
    sets: int = None
    reps: int = None
    rpe: int = None
    rest_seconds: int = None

    schema = programs_ns.model('ProgramExerciseInput', {
        'name': fields.String(required=True, description='Exercise name', example='Bench Press'),
        'sets': fields.Integer(required=True, description='Number of sets', example=4),
        'reps': fields.Integer(required=True, description='Number of reps', example=8),
        'rpe': fields.Integer(description='Rate of perceived exertion (1–10)', example=7),
        'rest_seconds': fields.Integer(description='Rest time in seconds', example=90)
    })


@dataclass
class ProgramExerciseOutput:
    """Output Object for Program Exercise data."""

    name: str
    sets: int
    reps: int
    rpe: int
    rest_seconds: int
