from flask import Blueprint, request

from users.service import UsersService
from core.constants.globals import METHOD_POST


api_user_bp = Blueprint('user', __name__)
users_service = UsersService()


@api_user_bp.route("", methods=[METHOD_POST])
def user_crud():
    if request.method == METHOD_POST:
        return users_service.create_user()


@api_user_bp.route("/<username>")
def user_data(username):
    return users_service.get_user_data(username)
