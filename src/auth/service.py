from flask import jsonify, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

from .repository import UsersRepository
from core.constants.globals import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from core.constants.pages import PAGE_SIGNUP
from core.constants.messages import MSG_ERROR_USER_TAKEN


class UsersService:

    def __init__(self):
        self.users_repository = UsersRepository()

    def login_user(self):
        data = request.get_json()
        request_username = data.get("username")
        request_password = data.get("password")
        user = self.users_repository.find_user_by_username(request_username)

        if user and check_password_hash(user.password, request_password):
            # return redirect(url_for(PAGE_DASHBOARD))
            return jsonify({"message": "User logged successfully.", "user_id": user.id}), HTTP_200_OK
        else:
            # return render_template(PAGE_LOGIN, error=MSG_ERROR_INVALID_CREDENTIALS)
            return jsonify({"message": "User invalid credentials."}), HTTP_401_UNAUTHORIZED

    def register_user(self):
        data = request.get_json()

        from dto.user import UserDto
        user_dto = UserDto()
        user_dto.set_username(data.get("username"))
        hashed_password = generate_password_hash(data.get("password"))
        user_dto.set_password(hashed_password)
        user_dto.set_email(data.get("email"))

        self.__check_if_user_exists(user_dto.get_username())
        self.users_repository.create_user(user_dto)

        return jsonify({"message": "User created successfully."}), HTTP_200_OK

    def __check_if_user_exists(self, username: str) -> str:
        if self.users_repository.find_user_by_username(username):
            return render_template(PAGE_SIGNUP, error=MSG_ERROR_USER_TAKEN)
