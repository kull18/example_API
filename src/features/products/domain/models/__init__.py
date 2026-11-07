from src.core.db import Base, engine
from src.features.products.domain.models.ProductModel import Product

__all__ = [
    "Base",
    "Product"
]

Base.metadata.create_all(bind=engine)