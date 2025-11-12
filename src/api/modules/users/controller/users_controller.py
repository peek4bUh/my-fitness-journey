from flask_restx import Resource

from api.core.namespaces import users_ns
from ..io.user import UserInput
from ..service import UsersService


@users_ns.route('')
class UsersController(Resource):

    @users_ns.expect(UserInput().schema, validate=True)
    def post(self):
        return UsersService().create_user()
