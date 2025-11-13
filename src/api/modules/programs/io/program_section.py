from dataclasses import dataclass
from flask_restx import fields
from typing import List

from api.core.namespaces import programs_ns
from .program_exercise import ProgramExerciseInput
from ..domain.entity.program_exercise_entity import ProgramExerciseEntity


@dataclass
class ProgramSectionInput:
    """Input Object for Program Section data."""

    name: str = None
    exercises: List[ProgramExerciseEntity] = None

    schema = programs_ns.model('ProgramSectionInput', {
        'name': fields.String(required=True, description='Section name (e.g., Day 1 - Upper Body)', example='Day 1 - Upper Body'),
        'exercises': fields.List(fields.Nested(ProgramExerciseInput().schema), required=True, description='List of exercises')
    })


@dataclass
class ProgramSectionOutput:
    """Output Object for Program Section data."""

    name: str
    exercises: List[ProgramExerciseEntity]
