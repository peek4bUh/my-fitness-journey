from typing import Any, Dict

from ..io.program.program_input import ProgramInput
from ..io.program_section.program_section_input import ProgramSectionInput
from ..io.program_exercise.program_exercise_input import ProgramExerciseInput
from ..io.program.program_output import ProgramOutput
from ..io.program_section.program_section_output import ProgramSectionOutput
from ..io.program_exercise.program_exercise_output import ProgramExerciseOutput
from ..domain.entity.program_entity import ProgramEntity


class ProgramMapper:

    def to_program_output(self, model: ProgramEntity) -> ProgramOutput:
        program_output = ProgramOutput(
            id=model.program_id,
            title=model.title,
            description=model.description,
            duration_weeks=model.duration_weeks,
            sections=[
                ProgramSectionOutput(
                    name=section.name,
                    exercises=[
                        ProgramExerciseOutput(
                            name=exercise.name,
                            sets=exercise.sets,
                            reps=exercise.reps,
                            rpe=exercise.rpe,
                            rest_seconds=exercise.rest_seconds
                        ).__dict__
                        for exercise in section.exercises
                    ]
                ).__dict__
                for section in model.sections
            ]
        ).__dict__

        return program_output

    def to_program_input(self, payload: Dict[str, Any]) -> ProgramInput:
        program_input = ProgramInput(
            title=payload.get("title"),
            description=payload.get("description"),
            duration_weeks=payload.get("duration_weeks"),
            sections=[
                ProgramSectionInput(
                    name=section.get("name"),
                    exercises=[
                        ProgramExerciseInput(
                            name=exercise.get("name"),
                            sets=exercise.get("sets"),
                            reps=exercise.get("reps"),
                            rpe=exercise.get("rpe"),
                            rest_seconds=exercise.get("rest_seconds")
                        )
                        for exercise in section.get("exercises")
                    ]
                )
                for section in payload.get("sections")
            ]
        )

        return program_input
