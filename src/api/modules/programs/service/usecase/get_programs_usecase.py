from shared.enum.http import HTTP
from ..mappers import ProgramMapper
from ...domain.repository import ProgramsRepository
from api.modules.programs.service.mappers import ProgramMapper
from ..mappers import ProgramMapper
from ...domain.repository import ProgramsRepository


class GetProgramsUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self) -> None:
        programs = self.programs_repository.find_all()

        if not programs:
            return None

        output = [self.program_mapper.to_program_output(p) for p in programs]

        return output, HTTP.Status.OK.value
