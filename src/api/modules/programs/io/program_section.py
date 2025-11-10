from typing import List

from .program_exercise import ProgramExerciseDto


class ProgramSectionDto:
    """Data Transfer Object for Program Section data."""

    def __init__(self, name: str, exercises: List[ProgramExerciseDto]):
        self.name = name
        self.exercises = exercises
