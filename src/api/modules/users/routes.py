from flask_restx import Resource, fields


from api.core.decorators.auth import require_api_key
from api.core.namespaces import users_ns
from api.config import api_restx
from api.modules.users.io.user import UserInput, UserOutput
from api.modules.users.service import UsersService


@users_ns.route('')
class UserCRUD(Resource):

    @users_ns.expect(UserInput().schema, validate=True)
    def post(self):
        return UsersService().create_user()


@users_ns.route('/user')
class UserData(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @api_restx.response(200, "OK", UserOutput().schema)
    @require_api_key
    def get(self):
        return UsersService().get_user_data()
