from app.core.http import Status
from app.domain.repository.programs_repository import ProgramsRepository
from app.service.mappers.program import ProgramMapper


class CreateProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self, payload: dict) -> None:
        input = self.program_mapper.to_input(payload)
        self.programs_repository.add_program(input)

        return {"message": "Program created successfully."}, Status.CREATED.value
