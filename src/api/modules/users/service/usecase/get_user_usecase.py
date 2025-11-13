from shared.enum.http import HTTP
from ...domain.repository import UsersRepository
from ..mappers import UserMapper


class GetUserUseCase:

    def __init__(self):
        self.users_repository = UsersRepository()
        self.user_mapper = UserMapper()

    def execute(self) -> None:
        user = self.users_repository.find_user()

        if not user:
            return None

        return self.user_mapper.to_user_output(user), HTTP.Status.OK.value
