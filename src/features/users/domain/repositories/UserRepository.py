from src.features.users.domain.schemas.UserSchema import ChangePasswordModel
from src.features.users.domain.schemas.UserSchema import LoginModel
from src.features.users.domain.schemas.UserSchema import CreateUser
from abc import abstractmethod
from src.features.users.domain.models.UserModel import User

class UserRepository:

    @abstractmethod
    def create_user(self, user: CreateUser):
        ...

    @abstractmethod
    def search_email(self, email: str):
        ...

    @abstractmethod
    def login(self, login_request: LoginModel):
        ...
    @abstractmethod
    def change_password(self, change_password_model: ChangePasswordModel):
        ...

