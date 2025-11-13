from flask_restx import fields

from api.core.namespaces import programs_ns


class ProgramExerciseInput:
    """Input Object for Program Exercise data."""

    schema = programs_ns.model('ProgramExerciseInput', {
        'name': fields.String(required=True, description='Exercise name', example='Bench Press'),
        'sets': fields.Integer(required=True, description='Number of sets', example=4),
        'reps': fields.Integer(required=True, description='Number of reps', example=8),
        'rpe': fields.Integer(description='Rate of perceived exertion (1–10)', example=7),
        'rest_seconds': fields.Integer(description='Rest time in seconds', example=90)
    })
