from typing import List
from flask import g

from ..io.program import ProgramInput
from .entity.program_entity import ProgramEntity
from .entity.program_section_entity import ProgramSectionEntity
from .entity.program_exercise_entity import ProgramExerciseEntity


class ProgramsRepository:

    def add_program(self, input: ProgramInput) -> None:
        new_program = ProgramEntity(
            user_id=g.get("user_id"),
            title=input.get_title(),
            description=input.get_description(),
            duration_weeks=input.get_duration_weeks(),
            sections=[
                ProgramSectionEntity(
                    name=section.get_name(),
                    exercises=[
                        ProgramExerciseEntity(
                            name=exercise.get_name(),
                            sets=exercise.get_sets(),
                            reps=exercise.get_reps(),
                            rpe=exercise.get_rpe(),
                            rest_seconds=exercise.get_rest_seconds()
                        )
                        for exercise in section.get_exercises()
                    ]
                )
                for section in input.get_sections()
            ]
        )

        from api.core.extensions import db
        db.session.add(new_program)
        db.session.commit()

    def find_by_id(self, program_id) -> ProgramEntity:
        return ProgramEntity.query.filter_by(user_id=g.get('user_id'), program_id=program_id).first()

    def find_all(self) -> List[ProgramEntity]:
        return ProgramEntity.query.filter_by(user_id=g.get('user_id')).all()
