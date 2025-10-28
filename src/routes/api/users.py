from flask import render_template, request

from services.users_service import UsersService
from globals import METHOD_GET, METHOD_POST, PAGE_LOGIN, PAGE_SIGNUP
from flask import Blueprint


user_bp = Blueprint('user', __name__)
users_service = UsersService()


@user_bp.route("/login", methods=[METHOD_POST])
def login():
    return users_service.login_user()


@user_bp.route('/register', methods=[METHOD_POST])
def register():
    return users_service.register_user()
