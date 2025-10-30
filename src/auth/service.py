from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from .repository import AuthRepository
from users.repository import UsersRepository
from core.constants.globals import HTTP_200_OK, HTTP_401_UNAUTHORIZED


class AuthService:

    def __init__(self):
        self.auth_repository = AuthRepository()
        self.users_repository = UsersRepository()

    def login_user(self):
        data = request.get_json()
        user = self.users_repository.find_by_username(data.get("username"))

        if user and check_password_hash(user.password, data.get("password")):
            self.auth_repository.login_user(user.id)
            return jsonify({"message": f"User {user.username} logged in successfully."}), HTTP_200_OK
        else:
            return jsonify({"message": "User invalid credentials."}), HTTP_401_UNAUTHORIZED

    def logout_user(self):
        data = request.get_json()
        user = self.users_repository.find_by_username(data.get("username"))
        self.auth_repository.logout_user()

        return jsonify({"message": f"User {user.username} logged out successfully."}), HTTP_200_OK
