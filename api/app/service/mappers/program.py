from typing import Any, Dict

from app.io.program import ProgramInput, ProgramOutput
from app.io.program_section import ProgramSectionInput, ProgramSectionOutput
from app.io.program_exercise import ProgramExerciseInput, ProgramExerciseOutput
from app.domain.entity.program import ProgramEntity


class ProgramMapper:

    def to_output(self, model: ProgramEntity) -> ProgramOutput:
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

    def to_input(self, payload: Dict[str, Any]) -> ProgramInput:
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
