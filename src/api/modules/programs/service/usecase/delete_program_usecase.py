from shared.enum.http import Status
from ...domain.repository import ProgramsRepository


class DeleteProgramUseCase:

    def __init__(self):
        self.programs_repository = ProgramsRepository()

    def execute(self, program_id: int) -> None:
        self.programs_repository.remove(program_id)
        return {"message": "Program deleted successfully."}, Status.OK.value
