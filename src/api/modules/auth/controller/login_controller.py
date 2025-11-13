from flask_restx import Resource

from api.core.namespaces import auth_ns
from api.modules.users.io.login_user.login_user_output import LoginUserOutput
from ..service import AuthService


@auth_ns.route('/login')
class Login(Resource):

    @auth_ns.expect(LoginUserOutput().schema, validate=True)
    def post(self):
        """Login an user"""
        return AuthService().login_user()
