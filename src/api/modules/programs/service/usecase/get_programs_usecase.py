from shared.enum.http import HTTP
from ...domain.repository import ProgramsRepository
from ..mappers.program import ProgramMapper


class GetProgramsUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self) -> None:
        programs = self.programs_repository.find_all()

        if not programs:
            return None

        output = [self.program_mapper.to_output(p) for p in programs]

        return output, HTTP.Status.OK.value
