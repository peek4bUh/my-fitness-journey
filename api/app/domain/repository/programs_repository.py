from typing import List
from flask import current_app, g

from app.io.program import ProgramInput
from app.domain.entity.program import ProgramEntity, ProgramSectionEntity, ProgramExerciseEntity


class ProgramsRepository:

    def add_program(self, input: ProgramInput) -> None:
        new_program = ProgramEntity(
            user_id=g.get("user_id"),
            title=input.title,
            description=input.description,
            duration_weeks=input.duration_weeks,
            sections=[
                ProgramSectionEntity(
                    name=section.name,
                    exercises=[
                        ProgramExerciseEntity(
                            name=exercise.name,
                            sets=exercise.sets,
                            reps=exercise.reps,
                            rpe=exercise.rpe,
                            rest_seconds=exercise.rest_seconds
                        )
                        for exercise in section.exercises
                    ]
                )
                for section in input.sections
            ]
        )

        from api.core.extensions import db
        db.session.add(new_program)
        db.session.commit()

    def find_by_id(self, program_id) -> ProgramEntity:
        return ProgramEntity.query.filter_by(user_id=g.get('user_id'), program_id=program_id).first()

    def find_all(self) -> List[ProgramEntity]:
        return ProgramEntity.query.filter_by(user_id=g.get('user_id')).all()

    def remove(self, program_id: int) -> None:
        """Delete a program owned by the current user."""
        program = ProgramEntity.query.filter_by(
            user_id=g.get('user_id'), program_id=program_id).first()

        from api.core.extensions import db
        db.session.delete(program)
        db.session.commit()
