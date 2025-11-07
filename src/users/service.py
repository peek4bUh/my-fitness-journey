from flask import jsonify, request
from werkzeug.security import generate_password_hash

from dto.user import UserOutput
from .repository import UsersRepository
from core.constants.globals import HTTP_201_CREATED, HTTP_409_CONFLICT


class UsersService:

    def __init__(self):
        self.users_repository = UsersRepository()

    def create_user(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        from dto.user import UserDto
        user_dto = UserDto()
        user_dto.set_username(username)
        hashed_password = generate_password_hash(password)
        user_dto.set_password(hashed_password)
        user_dto.set_email(data.get("email"))

        if self.users_repository.find_by_username(user_dto.get_username()) or \
           self.users_repository.find_by_email(user_dto.get_email()):
            return jsonify({"message": "User or email already exists."}), HTTP_409_CONFLICT

        self.users_repository.create_user(user_dto)

        return {"message": "User created successfully."}, HTTP_201_CREATED

    def get_user_data(self):
        user = self.users_repository.find_user()

        if not user:
            return None

        return user.to_dict()
