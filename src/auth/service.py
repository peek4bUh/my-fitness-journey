from flask import request
from werkzeug.security import check_password_hash

from users.repository import UsersRepository


class AuthService:

    def __init__(self):
        self.users_repository = UsersRepository()

    def login_user(self):
        data = request.get_json()
        user = self.users_repository.find_by_username(data.get("username"))

        if user and check_password_hash(user.password, data.get("password")):
            return {"user": user.to_dict(), "message": f"User {user.username} logged in successfully."}

        return {"message": "User invalid credentials."}, 401

    def logout_user(self):
        data = request.get_json()
        user = self.users_repository.find_by_username(data.get("username"))
        return {"message": f"User {user.username} logged out successfully."}
