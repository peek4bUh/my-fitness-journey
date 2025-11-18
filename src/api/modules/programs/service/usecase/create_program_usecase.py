from shared.enum.http import Status
from ...domain.repository import ProgramsRepository
from ..mappers.program import ProgramMapper


class CreateProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self, payload: dict) -> None:
        input = self.program_mapper.to_input(payload)
        self.programs_repository.add_program(input)

        return {"message": "Program created successfully."}, Status.CREATED.value
