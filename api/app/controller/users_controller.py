from flask_restx import Resource

from ..core.namespaces import users_ns
from ..io.user.user_input import UserInput
from ..service.usecase.create_user_usecase import CreateUserUseCase


@users_ns.route('')
class UsersController(Resource):

    @users_ns.expect(UserInput().schema, validate=True)
    def post(self):
        return CreateUserUseCase().execute(users_ns.payload)
