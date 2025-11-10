from flask import jsonify, request
from werkzeug.security import generate_password_hash

from .repository import UsersRepository
from .io.user import UserDto
from shared.enum.http import HTTP


class UsersService:

    def __init__(self):
        self.users_repository = UsersRepository()

    def create_user(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data.get("password"))
        user_dto = UserDto(data.get("username"),
                           hashed_password, data.get("email"))

        if self.users_repository.find_by_username(user_dto.get_username()) or \
           self.users_repository.find_by_email(user_dto.get_email()):
            return jsonify({"message": "User or email already exists."}), HTTP.Status.CONFLICT.value

        self.users_repository.create_user(user_dto)

        return {"message": "User created successfully."}, HTTP.Status.CREATED.value

    def get_user_data(self):
        user = self.users_repository.find_user()

        if not user:
            return None

        return user.to_dict()
