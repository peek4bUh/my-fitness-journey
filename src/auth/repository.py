from dto.user import UserDto
from .model import UserModel


class UsersRepository:

    def create_user(self, user: UserDto) -> None:
        new_user = UserModel(username=user.username,
                             password=user.password,
                             email=user.email)

        from database import db
        db.session.add(new_user)
        db.session.commit()

    def find_user_by_username(self, username: str) -> UserModel:
        return UserModel.query.filter_by(username=username).first()
