from flask import g

from ..io.user.user_input import UserInput
from .entity.user_entity import UserEntity
from api.core.extensions import login_manager


class UsersRepository:

    def add_user(self, user: UserInput) -> None:
        new_user = UserEntity(username=user.username,
                              password=user.password,
                              email=user.email)

        from api.core.extensions import db
        db.session.add(new_user)
        db.session.commit()

    def find_by_username(self, username: str) -> UserEntity:
        return UserEntity.query.filter_by(username=username).first()

    def find_by_email(self, email: str) -> UserEntity:
        return UserEntity.query.filter_by(email=email).first()

    def find_user(self) -> UserEntity:
        return UserEntity.query.filter_by(api_token=g.get('api_key')).first()

    # Load user for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return UserEntity.query.get(int(user_id))
