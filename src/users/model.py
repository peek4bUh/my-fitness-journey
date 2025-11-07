from flask_login import UserMixin
from sqlalchemy import DateTime, func
from sqlalchemy.orm import mapped_column
import secrets

from core.extensions import db


class UserModel(UserMixin, db.Model):

    __tablename__ = 'user'

    id = mapped_column(db.Integer, primary_key=True)
    username = mapped_column(db.String, unique=True, nullable=False)
    password = mapped_column(db.String, nullable=False)
    email = mapped_column(db.String, unique=True, nullable=False)
    api_token = mapped_column(db.String(
        64), unique=True, nullable=True, default=lambda: secrets.token_hex(32))
    created_at = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
