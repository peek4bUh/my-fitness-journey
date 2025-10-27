from services.user_service import UserService

from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/users')
def get_users():
    return UserService.get_users()
