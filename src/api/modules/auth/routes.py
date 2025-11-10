from flask_restx import Resource, fields

from .service import AuthService
from api.config import api_restx


ns = api_restx.namespace(name="Authentication Operations", path="/auth")
auth_service = AuthService()

auth_login_model = ns.model('AuthLogin', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password')
})


@ns.route('/login')
class Login(Resource):

    @ns.expect(auth_login_model, validate=True)
    def post(self):
        """Login an user"""
        return auth_service.login_user()


@ns.route('/logout')
class Logout(Resource):

    def post(self):
        """Logout an user"""
        return self.auth_service.logout_user()
