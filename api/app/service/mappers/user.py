from werkzeug.security import generate_password_hash

from ...domain.entity.user_entity import UserEntity
from ...io.user.user_input import UserInput
from ...io.user.user_output import UserOutput


class UserMapper:

    def to_output(self, model: UserEntity) -> UserOutput:
        user_output = UserOutput(
            username=model.username,
            email=model.email
        ).__dict__

        return user_output

    def to_input(self, payload: dict) -> UserInput:
        user_input = UserInput(
            username=payload.get("username"),
            email=payload.get("email"),
            password=generate_password_hash(payload.get("password"))
        )

        return user_input
