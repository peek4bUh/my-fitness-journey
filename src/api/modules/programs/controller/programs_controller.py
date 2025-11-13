from flask_restx import Resource

from api.core.decorators.auth import require_api_key
from api.config import api_restx
from api.core.namespaces import programs_ns
from ..service.usecase.create_program_usecase import CreateProgramUseCase
from ..service.usecase.get_programs_usecase import GetProgramsUseCase
from ..io.program.program_input import ProgramInput


@programs_ns.route('')
class ProgramsController(Resource):

    @programs_ns.doc(parser=api_restx.parser())
    @require_api_key
    def get(self):
        return GetProgramsUseCase().execute()

    @programs_ns.expect(ProgramInput().schema, validate=True)
    @programs_ns.response(201, 'Program created successfully')
    @require_api_key
    def post(self):
        return CreateProgramUseCase().execute(programs_ns.payload)
