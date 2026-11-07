
from src.features.users.domain.schemas.UserSchema import LoginModel
from src.features.users.domain.schemas.UserSchema import CreateUser
from src.features.users.domain.repositories import UserRepository

class UserUseCases:

    def __init__(self, repository: UserRepository):
        self.__repo = repository

    def create_user(self, user: CreateUser):
        return self.__repo.create_user(user)
    
    def login(self, login_model: LoginModel):
        """
            aun sin implementar, falta algunas cosas o me da hueva
        """
        pass