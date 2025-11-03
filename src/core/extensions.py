from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

api = Api(
    title="MyFitnessJourney",
    version="0.0.1",
    doc="/api/v0/schema/ui",
    prefix="/api/v0"
)
