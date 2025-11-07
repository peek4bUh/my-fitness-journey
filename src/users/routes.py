from flask_restx import Resource, fields

from core.decorators import require_api_key
from users.service import UsersService
from core.extensions import api


ns = api.namespace(name="Users Operations", path="/users")
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

    @api.doc(parser=api.parser())
    @require_api_key
    def get(self):
        return users_service.get_user_data()
