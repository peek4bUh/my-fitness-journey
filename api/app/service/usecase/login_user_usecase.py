from werkzeug.security import check_password_hash

from app.core.http import Status
from app.service.mappers.login_user import LoginUserMapper
from app.domain.repository.users_repository import UsersRepository


class LoginUserUseCase:

    def __init__(self):
        self.users_repository = UsersRepository()
        self.login_user_mapper = LoginUserMapper()

    def login_user(self, payload: dict):
        user = self.users_repository.find_by_username(payload.get("username"))

        if user and check_password_hash(user.password, payload.get("password")):
            return {
                "user": self.login_user_mapper.to_output(user),
                "message": f"User {user.username} logged in successfully."
            }, Status.OK.value

        return {"message": "User invalid credentials."}, Status.UNAUTHORIZED.value
