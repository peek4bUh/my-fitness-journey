from sqlalchemy.orm import mapped_column

from database import db


class UserModel(db.Model):

    __tablename__ = 'user'

    id = mapped_column(db.Integer, primary_key=True)
    username = mapped_column(db.String, unique=True, nullable=False)
    password = mapped_column(db.String, nullable=False)
    email = mapped_column(db.String, unique=True, nullable=False)
