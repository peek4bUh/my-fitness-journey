from flask_restx import fields
from typing import List

from api.core.namespaces import programs_ns
from ..program_exercise.program_exercise_input import ProgramExerciseInput


class ProgramSectionInput:
    """Input Object for Program Section data."""

    schema = programs_ns.model('ProgramSectionInput', {
        'name': fields.String(required=True, description='Section name (e.g., Day 1 - Upper Body)', example='Day 1 - Upper Body'),
        'exercises': fields.List(fields.Nested(ProgramExerciseInput().schema), required=True, description='List of exercises')
    })

    def __init__(self, name: str = None, exercises: List[ProgramExerciseInput] = None):
        self.name = name
        self.exercises = exercises

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_exercises(self):
        return self.exercises

    def set_exercises(self, exercises):
        self.exercises = exercises

    def __repr__(self) -> str:
        name = repr(self.name)
        if self.exercises is None:
            exercises_info = "None"
        else:
            exercises_info = f"{len(self.exercises)} exercise(s)"
        return f"ProgramSectionDto(name={name}, exercises={exercises_info})"
