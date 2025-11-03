from flask_restx import Resource

from .service import AuthService
from core.extensions import api


ns = api.namespace("auth", description="Auth Operations")
auth_service = AuthService()


@ns.route('/login')
class Login(Resource):

    @api.doc(parser=api.parser())
    def post(self):
        """Login an user"""
        return auth_service.login_user()


@ns.route('/logout')
class Logout(Resource):

    @api.doc(parser=api.parser())
    def post(self):
        """Logout an user"""
        return self.auth_service.logout_user()
