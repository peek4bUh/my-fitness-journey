from app.core.http import Status
from app.domain.repository.users_repository import UsersRepository
from app.service.mappers.user import UserMapper


class GetUserUseCase:

    def __init__(self):
        self.users_repository = UsersRepository()
        self.user_mapper = UserMapper()

    def execute(self) -> None:
        user = self.users_repository.find_user()

        if not user:
            return None

        return self.user_mapper.to_output(user), Status.OK.value
