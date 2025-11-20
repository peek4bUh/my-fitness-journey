from ...domain.entity.user_entity import UserEntity
from ...io.login_user.login_user_output import LoginUserOutput


class LoginUserMapper:

    def to_output(self, model: UserEntity) -> LoginUserOutput:
        login_user_output = LoginUserOutput(
            id=model.user_id,
            username=model.username,
            email=model.email
        ).__dict__

        return login_user_output
