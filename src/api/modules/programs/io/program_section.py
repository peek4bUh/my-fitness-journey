from typing import List

from .program_exercise import ProgramExerciseDto


class ProgramSectionDto:
    """Data Transfer Object for Program Section data."""

    def __init__(self, name: str = None, exercises: List[ProgramExerciseDto] = None):
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
