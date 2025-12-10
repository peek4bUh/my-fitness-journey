from flask_restx import Resource

from ..core.decorators import require_api_key
from ..core.namespaces import users_ns
from ..core.config import api_restx
from ..io.user.user_output import UserOutput
from ..service.usecase.get_user_usecase import GetUserUseCase


@users_ns.route('/user')
class UserController(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @api_restx.response(200, "OK", UserOutput().schema)
    @require_api_key
    def get(self):
        return GetUserUseCase().execute()
