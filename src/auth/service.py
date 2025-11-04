from flask import current_app, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from users.repository import UsersRepository
from core.constants.globals import HTTP_200_OK, HTTP_401_UNAUTHORIZED


class AuthService:

    def __init__(self):
        self.users_repository = UsersRepository()

    def login_user(self):
        data = request.get_json()
        user = self.users_repository.find_by_username(data.get("username"))

        if user and check_password_hash(user.password, data.get("password")):
            return {"message": f"User {user.username} logged in successfully."}

        return {"message": "User invalid credentials."}

    def logout_user(self):
        data = request.get_json()
        user = self.users_repository.find_by_username(data.get("username"))
        return {"message": f"User {user.username} logged out successfully."}
