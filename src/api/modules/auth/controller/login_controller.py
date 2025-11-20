from flask_restx import Resource

from api.core.namespaces import auth_ns
from api.modules.users.io.login_user.login_user_output import LoginUserOutput
from ..service.usecase.login_user_usecase import LoginUserUseCase


@auth_ns.route('/login')
class Login(Resource):

    @auth_ns.expect(LoginUserOutput().schema, validate=True)
    def post(self):
        """Login an user"""
        return LoginUserUseCase().login_user(auth_ns.payload)
