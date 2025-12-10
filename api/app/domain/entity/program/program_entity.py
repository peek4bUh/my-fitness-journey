from typing import List
from sqlalchemy import Date, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.extensions import db


class ProgramEntity(db.Model):

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
    sections: Mapped[List['ProgramSectionEntity']] = relationship(
        back_populates="program",
        cascade="all, delete-orphan"
    )
