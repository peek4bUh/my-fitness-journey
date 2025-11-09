from dto.program import ProgramDto
from programs.model import ProgramModel


class ProgramsRepository:

    def add_program(self, program: ProgramDto) -> None:
        new_program = ProgramModel.from_dto(program)

        from core.extensions import db
        db.session.add(new_program)
        db.session.commit()
