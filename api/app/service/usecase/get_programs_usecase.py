from app.core.http import Status
from app.domain.repository.programs_repository import ProgramsRepository
from app.service.mappers.program import ProgramMapper


class GetProgramsUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self) -> None:
        programs = self.programs_repository.find_all()

        if not programs:
            return None

        output = [self.program_mapper.to_output(p) for p in programs]

        return output, Status.OK.value
