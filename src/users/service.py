from flask import jsonify, render_template, request
from werkzeug.security import generate_password_hash

from .repository import UsersRepository
from core.constants.globals import HTTP_200_OK, HTTP_409_CONFLICT


class UsersService:

    def __init__(self):
        self.users_repository = UsersRepository()

    def create_user(self):
        data = request.get_json()

        from dto.user import UserDto
        user_dto = UserDto()
        user_dto.set_username(data.get("username"))
        hashed_password = generate_password_hash(data.get("password"))
        user_dto.set_password(hashed_password)
        user_dto.set_email(data.get("email"))

        if self.users_repository.find_by_username(user_dto.get_username()) or \
           self.users_repository.find_by_email(user_dto.get_email()):
            return jsonify({"message": "User or email already exists."}), HTTP_409_CONFLICT

        self.users_repository.create_user(user_dto)

        return jsonify({"message": "User created successfully."}), HTTP_200_OK
