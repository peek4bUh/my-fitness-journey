from flask_restx import Resource

from app.core.decorators import require_api_key
from app.core.config import api_restx
from app.core.namespaces import programs_ns
from app.service.usecase.create_program_usecase import CreateProgramUseCase
from app.service.usecase.get_programs_usecase import GetProgramsUseCase
from app.io.program import ProgramInput


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
