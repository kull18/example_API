from abc import abstractmethod
from src.features.products.domain.schemas.ProductSchema import ProductCreate, ProductUpdate
from src.features.products.domain.models.ProductModel import Product
from fastapi import UploadFile

class ProductRepository:

    @abstractmethod
    def get_all_products(self) -> list[Product]:
        ...
    
    @abstractmethod
    def get_product_by_id(self, id: int) -> Product:
        ...
    
    @abstractmethod
    async def create_product(self, name: str, price: float, description: str, image: UploadFile):
        ...
    
    @abstractmethod
    def update_product(self, id: int, product: ProductUpdate):
        ...
    
    @abstractmethod
    def delete_product(self, id: int):
        ...