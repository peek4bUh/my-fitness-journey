from flask import Blueprint

from services.auth_service import AuthService
from config.constants.globals import METHOD_GET, METHOD_POST


auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login", methods=[METHOD_GET, METHOD_POST])
def login_user():
    return AuthService.login_user()


@auth_bp.route('/register', methods=[METHOD_GET, METHOD_POST])
def register_user():
    return AuthService.register_user()
