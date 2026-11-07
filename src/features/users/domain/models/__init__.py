from src.core.db import Base, engine
from src.features.users.domain.models.UserModel import User

__all__ = [
    "Base",
    "User"
]

Base.metadata.create_all(bind=engine)