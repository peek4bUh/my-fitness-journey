from flask_restx import Resource

from api.core.decorators.auth import require_api_key
from api.config import api_restx
from api.core.namespaces import programs_ns
from ..service.usecase.get_program_usecase import GetProgramUseCase


@programs_ns.route('/<int:programId>')
class ProgramByIdController(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @require_api_key
    def get(self, programId):
        return GetProgramUseCase().execute(programId)
