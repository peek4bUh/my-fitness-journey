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

    def __init__(
            self,
            name: str = None,
            sets: int = None,
            reps: int = None,
            rpe: int = None,
            rest_seconds: int = None):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.rpe = rpe
        self.rest_seconds = rest_seconds

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sets(self):
        return self.sets

    def set_sets(self, sets):
        self.sets = sets

    def get_reps(self):
        return self.reps

    def set_reps(self, reps):
        self.reps = reps

    def get_rpe(self):
        return self.rpe

    def set_rpe(self, rpe):
        self.rpe = rpe

    def get_rest_seconds(self):
        return self.rest_seconds

    def set_rest_seconds(self, rest_seconds):
        self.rest_seconds = rest_seconds

    def __repr__(self) -> str:
        return (
            f"ProgramExerciseDto(name={repr(self.name)}, sets={repr(self.sets)}, "
            f"reps={repr(self.reps)}, rpe={repr(self.rpe)}, rest_seconds={repr(self.rest_seconds)})"
        )
