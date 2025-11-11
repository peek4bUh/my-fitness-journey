from typing import Any, Dict

from api.modules.programs.io.program import ProgramDto, ProgramOutput
from api.modules.programs.io.program_exercise import ProgramExerciseDto, ProgramExerciseOutput
from api.modules.programs.io.program_section import ProgramSectionDto, ProgramSectionOutput
from api.modules.programs.model import ProgramModel


class ProgramMapper:

    def to_program_output(self, model: ProgramModel) -> ProgramOutput:
        sections = []

        for section in model.sections:
            exercises = []

            for exercise in section.exercises:
                exercises.append(
                    ProgramExerciseOutput(
                        name=exercise.name,
                        sets=exercise.sets,
                        reps=exercise.reps,
                        rpe=exercise.rpe,
                        rest_seconds=exercise.rest_seconds
                    ).to_dict()
                )

            sections.append(
                ProgramSectionOutput(
                    name=section.name,
                    exercises=exercises
                ).to_dict()
            )

        program_output = ProgramOutput(
            id=model.program_id,
            title=model.title,
            description=model.description,
            duration_weeks=model.duration_weeks,
            sections=sections
        )

        return program_output.to_dict()

    def to_program_dto(self, payload: Dict[str, Any]) -> ProgramDto:
        sections = []

        for section in payload.get("sections"):
            exercises = []

            for exercise in section.get("exercises"):
                exercises.append(
                    ProgramExerciseDto(
                        name=exercise.get("name"),
                        sets=exercise.get("sets"),
                        reps=exercise.get("reps"),
                        rpe=exercise.get("rpe"),
                        rest_seconds=exercise.get("rest_seconds")
                    )
                )

            sections.append(
                ProgramSectionDto(
                    name=section.get("name"),
                    exercises=exercises

                )
            )

        program_dto = ProgramDto(
            title=payload.get("title"),
            description=payload.get("description"),
            duration_weeks=payload.get("duration_weeks"),
            sections=sections
        )

        return program_dto
