from shared.enum.http import HTTP
from api.modules.programs.service.mappers import ProgramMapper
from ..mappers import ProgramMapper
from ...domain.repository import ProgramsRepository


class CreateProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self, payload: dict) -> None:
        program_dto = self.program_mapper.to_program_dto(payload)
        self.programs_repository.add_program(program_dto)
        return {"message": "Program created successfully."}, HTTP.Status.CREATED.value
