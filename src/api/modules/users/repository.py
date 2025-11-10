from flask import g

from .io.user import UserDto
from .model import UserModel
from api.core.extensions import login_manager


class UsersRepository:

    def create_user(self, user: UserDto) -> None:
        new_user = UserModel(username=user.username,
                             password=user.password,
                             email=user.email)

        from api.core.extensions import db
        db.session.add(new_user)
        db.session.commit()

    def find_by_username(self, username: str) -> UserModel:
        return UserModel.query.filter_by(username=username).first()

    def find_by_email(self, email: str) -> UserModel:
        return UserModel.query.filter_by(email=email).first()

    def find_user(self) -> UserModel:
        return UserModel.query.filter_by(api_token=g.get('api_key')).first()

    # Load user for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(int(user_id))
