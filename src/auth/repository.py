from flask import jsonify, session

from users.model import UserModel
from core.constants.globals import HTTP_200_OK


class AuthRepository:

    def login_user(self, user_id: int):
        session.clear()
        session["user_id"] = user_id

    def logout_user(self):
        session.clear()
