from flask_restx import Resource

from users.service import UsersService
from core.extensions import api


ns = api.namespace(name="Users Operations", path="/users")
users_service = UsersService()


@ns.route('')
class UserCRUD(Resource):

    @api.doc(parser=api.parser())
    def post(self):
        return users_service.create_user()


@ns.route('/<username>')
class UserData(Resource):

    @api.doc(parser=api.parser())
    def get(self, username):
        return users_service.get_user_data(username)
