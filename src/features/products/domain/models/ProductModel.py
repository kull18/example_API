from src.core.db import Base
from sqlalchemy import String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):

    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)
    image: Mapped[str] = mapped_column(String(255))