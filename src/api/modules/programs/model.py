from __future__ import annotations
from typing import List
from flask import g
from sqlalchemy import Date, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from api.core.extensions import db


class ProgramModel(db.Model):

    __tablename__ = 'program'

    program_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.user_id"), nullable=False)
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
