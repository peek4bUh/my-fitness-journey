from shared.enum.http import HTTP
from ..mappers import ProgramMapper
from ...domain.repository import ProgramsRepository
from api.modules.programs.service.mappers import ProgramMapper
from ..mappers import ProgramMapper
from ...domain.repository import ProgramsRepository


class GetProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self, program_id: int) -> None:
        program = self.programs_repository.find_by_id(program_id)

        if not program:
            return None

        return self.program_mapper.to_program_output(program), HTTP.Status.OK.value
