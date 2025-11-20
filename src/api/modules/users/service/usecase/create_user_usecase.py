from shared.enum.http import Status
from ...domain.repository import UsersRepository
from ..mappers.user import UserMapper


class CreateUserUseCase:

    def __init__(self):
        self.users_repository = UsersRepository()
        self.user_mapper = UserMapper()

    def execute(self, payload: dict) -> None:
        user_input = self.user_mapper.to_input(payload)

        if self.users_repository.find_by_username(user_input.get_username()) or \
           self.users_repository.find_by_email(user_input.get_email()):
            return {"message": "User or email already exists."}, Status.CONFLICT.value

        self.users_repository.add_user(user_input)

        return {"message": "User created successfully."}, Status.CREATED.value
