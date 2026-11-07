from fastapi import Request
from src.features.products.domain.models.ProductModel import Product
from src.features.products.domain.schemas.ProductSchema import ProductCreate, ProductUpdate
from src.features.products.domain.repositories.ProductRepository import ProductRepository
from src.features.products.application.mappers.ProductMapper import to_product_response
from fastapi import File
from fastapi import UploadFile


class ProductUseCases:

    def __init__(self, repo: ProductRepository):
        self.__repo = repo

    def get_all_products(self) -> list[Product]:
        return  self.__repo.get_all_products()
    
    def get_product_by_id(self, id: int) -> Product:
        return self.__repo.get_product_by_id(id)
    
    async def create_product(self, request: Request,name: str, price: float, description: str, image: UploadFile):
        product =  await self.__repo.create_product(name=name, price=price, description=description, image=image)
        return to_product_response(product, request)
    
    def update_product(self, id: int, product: ProductUpdate):
        return self.__repo.update_product(id, product)
    
    def delete_product(self, id: int):
        return self.__repo.delete_product(id)    