from typing import List
from sqlalchemy import Date, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.extensions import db


class ProgramExerciseEntity(db.Model):

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

    section: Mapped['ProgramSectionEntity'] = relationship(
        back_populates="exercises")
