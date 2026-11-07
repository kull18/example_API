from fastapi import Request
from src.features.products.application.usecases.ProductUseCases import ProductUseCases
from src.features.products.domain.schemas.ProductSchema import ProductCreate, ProductUpdate
from src.features.products.infraestructure.repositories.ProductRepositoryImpl import ProductRepositoryImpl
from fastapi import UploadFile, File

class ProductController:


    def __init__(self):
        self.__repo = ProductRepositoryImpl()
        self.__use_cases = ProductUseCases(self.__repo)

    def get_all_products(self):
        return self.__use_cases.get_all_products()

    def get_product_by_id(self, id: int):
        return self.__use_cases.get_product_by_id(id)

    async def create_product(self, request: Request,name: str, price: float, description: str, image: UploadFile):
        return await self.__use_cases.create_product(request,name=name, price=price, description=description, image=image)

    def update_product(self, id: int, product: ProductUpdate):
        return self.__use_cases.update_product(id, product)

    def delete_product(self, id: int):
        return self.__use_cases.delete_product(id)    