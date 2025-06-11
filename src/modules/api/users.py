from flask import Blueprint, jsonify
from modules.models.user import UserModel

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/users')
def get_users():
    users = UserModel.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users])
