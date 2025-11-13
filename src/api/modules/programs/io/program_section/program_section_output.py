from typing import List

from ...domain.entity.program_exercise_entity import ProgramExerciseEntity


class ProgramSectionOutput:
    """Output Object for Program Section data."""

    def __init__(self, name: int = None, exercises: List[ProgramExerciseEntity] = None):
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
