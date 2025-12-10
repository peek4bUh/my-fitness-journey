from app.core.http import Status
from app.domain.repository.programs_repository import ProgramsRepository


class DeleteProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()

    def execute(self, program_id: int) -> None:
        self.programs_repository.remove(program_id)
        return {"message": "Program deleted successfully."}, Status.OK.value
