from flask_login import UserMixin
from sqlalchemy.orm import mapped_column

from core.extensions import db


class UserModel(UserMixin, db.Model):

    __tablename__ = 'user'

    id = mapped_column(db.Integer, primary_key=True)
    username = mapped_column(db.String, unique=True, nullable=False)
    password = mapped_column(db.String, nullable=False)
    email = mapped_column(db.String, unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
