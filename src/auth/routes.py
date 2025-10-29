from flask import Blueprint

from users.service import UsersService
from core.constants.globals import METHOD_POST


user_bp = Blueprint('user', __name__)
users_service = UsersService()


@user_bp.route("/login", methods=[METHOD_POST])
def login():
    return users_service.login_user()


@user_bp.route('/register', methods=[METHOD_POST])
def register():
    return users_service.register_user()


@user_bp.route('/')
def test():
    return {"message": "Hello World!"}
