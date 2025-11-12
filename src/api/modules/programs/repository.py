from flask import g

from .io.program import ProgramDto
from .model import ProgramExerciseModel, ProgramModel, ProgramSectionModel


class ProgramsRepository:

    def add_program(self, dto: ProgramDto) -> None:
        new_program = ProgramModel(
            user_id=g.get("user_id"),
            title=dto.get_title(),
            description=dto.get_description(),
            duration_weeks=dto.get_duration_weeks(),
            sections=[
                ProgramSectionModel(
                    name=section.get_name(),
                    exercises=[
                        ProgramExerciseModel(
                            name=exercise.get_name(),
                            sets=exercise.get_sets(),
                            reps=exercise.get_reps(),
                            rpe=exercise.get_rpe(),
                            rest_seconds=exercise.get_rest_seconds()
                        )
                        for exercise in section.get_exercises()
                    ]
                )
                for section in dto.get_sections()
            ]
        )

        from api.core.extensions import db
        db.session.add(new_program)
        db.session.commit()

    def find_by_id(self, program_id) -> ProgramModel:
        return ProgramModel.query.filter_by(user_id=g.get('user_id'), program_id=program_id).first()

    def find_all(self) -> ProgramModel:
        return ProgramModel.query.filter_by(user_id=g.get('user_id'))
