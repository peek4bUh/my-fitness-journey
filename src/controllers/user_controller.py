from flask import jsonify

from routes.blueprints import api_bp
from services.user_service import UserService


@api_bp.route('/users')
def get_users():
    return UserService.get_users()
