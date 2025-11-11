from api.modules.programs.mappers import ProgramMapper
from shared.enum.http import HTTP
from .repository import ProgramsRepository


class ProgramsService:

    def __init__(self):
        self.programs_repository = ProgramsRepository()
        self.program_mapper = ProgramMapper()

    def create_program(self, payload: dict):
        program_dto = self.program_mapper.to_program_dto(payload)
        self.programs_repository.add_program(program_dto)

        return {"message": "Program created successfully."}, HTTP.Status.CREATED.value

    def get_program(self, program_id: int):
        program = self.programs_repository.find_by_id(program_id)

        if not program:
            return None

        return self.program_mapper.to_program_output(program)
