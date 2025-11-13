from typing import List

from ...domain.dto.program_exercise_dto import ProgramExerciseDto


class ProgramSectionOutput:
    """Output Object for Program Section data."""

    def __init__(self, name: int = None, exercises: List[ProgramExerciseDto] = None):
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
