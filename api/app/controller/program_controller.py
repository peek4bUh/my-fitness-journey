from flask_restx import Resource

from app.core.decorators import require_api_key
from app.core.config import api_restx
from app.core.namespaces import programs_ns
from app.service.usecase.get_program_usecase import GetProgramUseCase
from app.service.usecase.delete_program_usecase import DeleteProgramUseCase


@programs_ns.route('/<int:programId>')
class ProgramByIdController(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @require_api_key
    def get(self, programId):
        return GetProgramUseCase().execute(programId)

    @api_restx.doc(parser=api_restx.parser())
    @require_api_key
    def delete(self, programId):
        return DeleteProgramUseCase().execute(programId)
