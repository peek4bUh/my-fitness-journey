from flask import Blueprint, request

from users.service import UsersService
from core.constants.globals import METHOD_GET, METHOD_POST


user_bp = Blueprint('user', __name__)
users_service = UsersService()


@user_bp.route("", methods=[METHOD_GET, METHOD_POST])
def crud():
    if request.method == METHOD_GET:
        return users_service.render_login_page()

    if request.method == METHOD_POST:
        return users_service.create_user()
