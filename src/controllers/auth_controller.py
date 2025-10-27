from flask import Blueprint, render_template, request

from services.auth_service import AuthService
from config.constants.globals import METHOD_GET, METHOD_POST
from config.constants.pages import PAGE_LOGIN, PAGE_SIGNUP


auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()


@auth_bp.route("/login", methods=[METHOD_GET, METHOD_POST])
def login():
    if request.method == METHOD_GET:
        return render_template(PAGE_LOGIN)

    if request.method == METHOD_POST:
        return auth_service.login_user()


@auth_bp.route('/register', methods=[METHOD_GET, METHOD_POST])
def register():
    if request.method == METHOD_GET:
        return render_template(PAGE_SIGNUP)

    if request.method == METHOD_POST:
        return auth_service.register_user()
