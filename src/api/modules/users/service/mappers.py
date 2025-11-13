from werkzeug.security import generate_password_hash

from api.modules.users.domain.entity.user_entity import UserEntity
from api.modules.users.io.user.user_input import UserInput
from ..io.user.user_output import UserOutput
from ..io.login_user.login_user_output import LoginUserOutput


class UserMapper:

    def to_user_output(self, model: UserEntity) -> UserOutput:
        user_output = UserOutput(
            username=model.username,
            email=model.email
        ).__dict__

        return user_output

    def to_user_input(self, payload: dict) -> UserInput:
        user_input = UserInput(
            username=payload.get("username"),
            email=payload.get("email"),
            password=generate_password_hash(payload.get("password"))
        )

        return user_input

    def to_login_user_output(self, model: UserEntity) -> LoginUserOutput:
        login_user_output = LoginUserOutput(
            id=model.user_id,
            username=model.username,
            email=model.email
        ).__dict__

        return login_user_output
