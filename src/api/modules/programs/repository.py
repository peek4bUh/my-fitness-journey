from flask import g

from dto.program import ProgramDto
from api.modules.programs.model import ProgramModel


class ProgramsRepository:

    def add_program(self, program: ProgramDto) -> None:
        new_program = ProgramModel.from_dto(program)

        from api.core.extensions import db
        db.session.add(new_program)
        db.session.commit()

    def find_program_by_id(self, program_id) -> ProgramModel:
        return ProgramModel.query.filter_by(user_id=g.get('user_id'), program_id=program_id).first()
