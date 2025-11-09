from flask import request
from core.constants.globals import HTTP_201_CREATED
from dto.program import ProgramDto, ProgramSectionDto, ProgramExerciseDto
from .repository import ProgramsRepository


class ProgramsService:

    def __init__(self):
        self.programs_repository = ProgramsRepository()

    def create_program(self, data: dict):
        sections = []

        for section in data.get("sections", []):
            exercises = [
                ProgramExerciseDto(
                    name=exercise["name"],
                    sets=exercise["sets"],
                    reps=exercise["reps"],
                    rpe=exercise.get("rpe"),
                    rest_seconds=exercise.get("rest_seconds")
                )
                for exercise in section.get("exercises", [])
            ]
            sections.append(
                ProgramSectionDto(
                    name=section["name"],
                    exercises=exercises
                )
            )

        program_dto = ProgramDto(
            title=data["title"],
            description=data["description"],
            duration_weeks=data["duration_weeks"],
            sections=sections
        )

        self.programs_repository.add_program(program_dto)

        return {"message": "Program created successfully."}, HTTP_201_CREATED

    def get_program(self, program_id: int):
        program = self.programs_repository.find_program_by_id(program_id)

        if not program:
            return None

        return program.to_dict()
