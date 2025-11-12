from typing import Any, Dict

from api.modules.programs.io.program import ProgramDto, ProgramOutput
from api.modules.programs.io.program_exercise import ProgramExerciseDto, ProgramExerciseOutput
from api.modules.programs.io.program_section import ProgramSectionDto, ProgramSectionOutput
from api.modules.programs.model import ProgramModel


class ProgramMapper:

    def to_program_output(self, model: ProgramModel) -> ProgramOutput:
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

    def to_program_dto(self, payload: Dict[str, Any]) -> ProgramDto:
        program_dto = ProgramDto(
            title=payload.get("title"),
            description=payload.get("description"),
            duration_weeks=payload.get("duration_weeks"),
            sections=[
                ProgramSectionDto(
                    name=section.get("name"),
                    exercises=[
                        ProgramExerciseDto(
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

        return program_dto
