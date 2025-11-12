from flask_restx import Resource

from ..service import AuthService
from ..schemas import login_input_schema
from api.core.namespaces import auth_ns


@auth_ns.route('/login')
class Login(Resource):

    @auth_ns.expect(login_input_schema, validate=True)
    def post(self):
        """Login an user"""
        return AuthService().login_user()
