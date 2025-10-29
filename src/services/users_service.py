from flask import jsonify, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from models.user import UserModel
from repository.users_repository import UsersRepository
from globals import (
    PAGE_DASHBOARD,
    PAGE_LOGIN,
    PAGE_SIGNUP,
    MSG_ERROR_INVALID_CREDENTIALS,
    MSG_ERROR_USER_TAKEN,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)


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
