from flask import jsonify

from models.user import UserModel


class UserService:

    @staticmethod
    def get_users():
        users = UserModel.query.all()
        return jsonify([{"id": u.id, "username": u.username} for u in users])
