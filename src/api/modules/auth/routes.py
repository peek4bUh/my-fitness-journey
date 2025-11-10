from flask_restx import Resource, fields

from .service import AuthService
from api.core.namespaces import auth_ns

auth_service = AuthService()

auth_login_model = auth_ns.model('AuthLogin', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password')
})


@auth_ns.route('/login')
class Login(Resource):

    @auth_ns.expect(auth_login_model, validate=True)
    def post(self):
        """Login an user"""
        return auth_service.login_user()


@auth_ns.route('/logout')
class Logout(Resource):

    def post(self):
        """Logout an user"""
        return self.auth_service.logout_user()
