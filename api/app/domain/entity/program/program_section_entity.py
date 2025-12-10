from typing import List
from sqlalchemy import Date, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.extensions import db


class ProgramSectionEntity(db.Model):

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
    program: Mapped['ProgramEntity'] = relationship(back_populates="sections")
    exercises: Mapped[List['ProgramExerciseEntity']] = relationship(
        back_populates="section",
        cascade="all, delete-orphan"
    )
