from  src.core.db import Base
from sqlalchemy import String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):

    __tablename__ = 'users'

    user_id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)