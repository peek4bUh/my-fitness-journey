from app.core.http import Status
from app.domain.repository.programs_repository import ProgramsRepository
from app.service.mappers.program import ProgramMapper


class GetProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def execute(self, program_id: int) -> None:
        program = self.programs_repository.find_by_id(program_id)

        if not program:
            return None

        return self.program_mapper.to_output(program), Status.OK.value
