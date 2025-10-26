from routes.blueprints import auth_bp
from services.auth_service import AuthService


@auth_bp.route("/login", methods=["GET", "POST"])
def login_user():
    return AuthService.login_user()


@auth_bp.route('/register', methods=["GET", "POST"])
def register_user():
    return AuthService.register_user()
