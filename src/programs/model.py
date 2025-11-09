from __future__ import annotations
from typing import List
from sqlalchemy import Date, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from core.extensions import db
from dto.program import ProgramDto


class ProgramModel(db.Model):

    __tablename__ = 'program'

    program_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    description: Mapped[str] = mapped_column(db.String, nullable=True)
    duration_weeks: Mapped[int] = mapped_column(db.Integer, nullable=False)
    created_at: Mapped[Date] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Relationships
    sections: Mapped[List['ProgramSectionModel']] = relationship(
        back_populates="program",
        cascade="all, delete-orphan"
    )

    def from_dto(dto: ProgramDto) -> ProgramModel:
        return ProgramModel(
            title=dto.title,
            description=dto.description,
            duration_weeks=dto.duration_weeks,
            sections=[
                ProgramSectionModel(
                    name=s.name,
                    exercises=[
                        ProgramExerciseModel(
                            name=e.name, sets=e.sets, reps=e.reps, rpe=e.rpe, rest_seconds=e.rest_seconds
                        )
                        for e in s.exercises
                    ]
                )
                for s in dto.sections
            ]
        )


class ProgramSectionModel(db.Model):

    __tablename__ = "program_section"

    program_section_id: Mapped[int] = mapped_column(primary_key=True)
    program_id: Mapped[int] = mapped_column(
        ForeignKey("program.program_id"), nullable=False)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    created_at: Mapped[Date] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Relationships
    program: Mapped['ProgramModel'] = relationship(back_populates="sections")
    exercises: Mapped[List['ProgramExerciseModel']] = relationship(
        back_populates="section",
        cascade="all, delete-orphan"
    )


class ProgramExerciseModel(db.Model):

    __tablename__ = 'program_exercise'

    program_exercise_id: Mapped[int] = mapped_column(
        db.Integer, primary_key=True)
    program_section_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey(
        'program_section.program_section_id'), nullable=False)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    sets: Mapped[int] = mapped_column(db.Integer, nullable=False)
    reps: Mapped[int] = mapped_column(db.Integer, nullable=False)
    rpe: Mapped[int] = mapped_column(db.Integer, nullable=False)
    rest_seconds: Mapped[int] = mapped_column(db.Integer, nullable=True)
    created_at: Mapped[Date] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    section: Mapped['ProgramSectionModel'] = relationship(
        back_populates="exercises")
