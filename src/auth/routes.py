from flask import Blueprint

from .service import AuthService
from core.constants.globals import METHOD_POST


api_auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()


@api_auth_bp.route("/login", methods=[METHOD_POST])
def login():
    return auth_service.login_user()


@api_auth_bp.route('/logout', methods=[METHOD_POST])
def logout():
    return auth_service.logout_user()
