from flask_restx import Resource

from api.core.decorators.auth import require_api_key
from api.config import api_restx
from api.core.namespaces import programs_ns
from ..service import ProgramsService
from ..schemas import program_input_schema


@programs_ns.route('')
class ProgramsController(Resource):

    @programs_ns.doc(parser=api_restx.parser())
    def get(self):
        pass

    @programs_ns.expect(program_input_schema, validate=True)
    @programs_ns.response(201, 'Program created successfully')
    @require_api_key
    def post(self):
        return ProgramsService().create_program(programs_ns.payload)
