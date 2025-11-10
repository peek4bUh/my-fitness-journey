from flask_restx import Resource, fields

from api.core.decorators.auth import require_api_key

from .service import ProgramsService
from .schemas import program_input_schema
from api.config import api_restx
from api.core.namespaces import programs_ns


@programs_ns.route('')
class Program(Resource):

    @programs_ns.doc(parser=api_restx.parser())
    def get(self):
        pass

    @programs_ns.expect(program_input_schema, validate=True)
    @programs_ns.response(201, 'Program created successfully')
    @require_api_key
    def post(self):
        return ProgramsService().create_program(programs_ns.payload)


@programs_ns.route('/<int:programId>')
class ProgramById(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @require_api_key
    def get(self, programId):
        return ProgramsService().get_program(programId)
