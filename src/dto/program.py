from __future__ import annotations
from typing import List


class ProgramDto:
    """Data Transfer Object for Program data."""

    def __init__(
            self,
            title: str,
            description: str,
            duration_weeks: int,
            sections: List[ProgramSectionDto]):
        self.title = title
        self.description = description
        self.duration_weeks = duration_weeks
        self.sections = sections


class ProgramSectionDto:
    """Data Transfer Object for Program Section data."""

    def __init__(self, name: str, exercises: List[ProgramExerciseDto]):
        self.name = name
        self.exercises = exercises


class ProgramExerciseDto:
    """Data Transfer Object for Program Exercise data."""

    def __init__(
            self,
            name: str,
            sets: int,
            reps: int,
            rpe: int,
            rest_seconds: int):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.rpe = rpe
        self.rest_seconds = rest_seconds
