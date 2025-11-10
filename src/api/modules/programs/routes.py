from flask import current_app, g
from flask_restx import Resource, fields

from api.core.decorators.auth import require_api_key

from .service import ProgramsService
from api.config import api_restx


ns = api_restx.namespace(name="Programs Operations", path="/programs")
programs_service = ProgramsService()

program_exercise_model = ns.model('ProgramExercise', {
    'name': fields.String(required=True, description='Exercise name', example='Bench Press'),
    'sets': fields.Integer(required=True, description='Number of sets', example=4),
    'reps': fields.Integer(required=True, description='Number of reps', example=8),
    'rpe': fields.Integer(description='Rate of perceived exertion (1–10)', example=7),
    'rest_seconds': fields.Integer(description='Rest time in seconds', example=90)
})

program_section_model = ns.model('ProgramSection', {
    'name': fields.String(required=True, description='Section name (e.g., Day 1 - Upper Body)', example='Day 1 - Upper Body'),
    'exercises': fields.List(fields.Nested(program_exercise_model), required=True, description='List of exercises')
})

program_model = ns.model('Program', {
    'title': fields.String(required=True, description='Program title', example='6-Week Beginner Strength Program'),
    'description': fields.String(required=True, description='Program description', example='A 6-week plan focusing on full-body strength.'),
    'duration_weeks': fields.Integer(required=True, description='Duration in weeks', example=6),
    'sections': fields.List(fields.Nested(program_section_model), required=True, description='Workout sections')
})


@ns.route('')
class Program(Resource):

    @api_restx.doc(parser=api_restx.parser())
    def get(self):
        pass

    @ns.expect(program_model, validate=True)
    @ns.response(201, 'Program created successfully')
    @require_api_key
    def post(self):
        return programs_service.create_program(ns.payload)


@ns.route('/<int:programId>')
class ProgramById(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @require_api_key
    def get(self, programId):
        return programs_service.get_program(programId)
