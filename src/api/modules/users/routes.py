from flask_restx import Resource, fields

from api.core.decorators.auth import require_api_key
from api.config import api_restx
from api.modules.users.service import UsersService


ns = api_restx.namespace(name="Users Operations", path="/users")
users_service = UsersService()

user_model = ns.model('User', {
    'username': fields.String(required=True, description='The user name'),
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password')
})


@ns.route('')
class UserCRUD(Resource):

    @ns.expect(user_model, validate=True)
    def post(self):
        return users_service.create_user()


@ns.route('/user')
class UserData(Resource):

    @api_restx.doc(parser=api_restx.parser())
    @require_api_key
    def get(self):
        return users_service.get_user_data()
