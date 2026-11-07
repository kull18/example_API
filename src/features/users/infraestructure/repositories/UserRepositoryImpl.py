from src.features.users.domain.schemas.UserSchema import CreateUser
from src.features.users.domain.repositories.UserRepository import UserRepository
from src.core.db import SessionLocal
from src.features.users.domain.models.UserModel import User
from fastapi import HTTPException
from src.core.logger import logger

class UserRepositoyImpl(UserRepository):

    def __init__(self):
        self.__conn = SessionLocal()

    def create_user(self, user: CreateUser):
        try:
            if self.search_email(user.email) is not None:
                raise HTTPException()

            new_user = User(
                username=user.username,
                password=user.password,
                email=user.email
            )

            self.__conn.add(new_user)
            self.__conn.commit()
            self.__conn.refresh(new_user)

            return new_user

        except Exception as e:
            logger.exception("error al crear usuario")
            return "error al crear usuario"

    def search_email(self, email: str):
        return self.__conn.query(User).filter(User.email == email)