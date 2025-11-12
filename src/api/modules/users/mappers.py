from api.modules.users.io.user import LoginUserOutput, UserOutput
from api.modules.users.model import UserModel


class UserMapper:

    def to_user_output(self, model: UserModel) -> UserOutput:
        user_output = UserOutput()
        user_output.set_username(model.username)
        user_output.set_email(model.email)

        return user_output.__dict__

    def to_login_user_output(self, model: UserModel) -> LoginUserOutput:
        login_user_output = LoginUserOutput()
        login_user_output.set_id(model.user_id)
        login_user_output.set_username(model.username)
        login_user_output.set_email(model.email)

        return login_user_output.__dict__
