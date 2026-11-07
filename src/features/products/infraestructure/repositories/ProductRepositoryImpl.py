from starlette.staticfiles import StaticFiles
from pathlib import Path
import shutil
from src.features.products.domain.repositories.ProductRepository import ProductRepository
from src.features.products.domain.models.ProductModel import Product
from src.features.products.domain.schemas.ProductSchema import ProductCreate, ProductUpdate
from src.core.db import SessionLocal
from src.core.handlers import strip_metadata
from fastapi import HTTPException, UploadFile, status
from src.core.logger import logger

class ProductRepositoryImpl(ProductRepository):

    def __init__(self):
        self.__conn = SessionLocal()

    def get_all_products(self) -> list[Product]:
        return self.__conn.query(Product).all()
    
    def get_product_by_id(self, id: int) -> Product:
        return self.__conn.query(Product).filter(Product.id == id).first()
    
    async def create_product(
        self, name: str, price: float, description: str, image: UploadFile
    ) -> Product:
     try:
        product = ProductCreate(
            name=name, price=price, description=description
        )
        content = await image.read()
        clean_bytes = strip_metadata(content, format="JPEG")

        upload_dir = Path("assets/products")
        upload_dir.mkdir(parents=True, exist_ok=True)

        filename = image.filename or "image.jpg"
        file_path = upload_dir / filename

        with file_path.open("wb") as f:
            f.write(clean_bytes)

        new_product = Product(
            name=product.name,
            price=product.price,
            description=product.description,
            image=str(file_path),
        )

        self.__conn.add(new_product)
        self.__conn.commit()
        self.__conn.refresh(new_product)
        logger.success("Producto creado...")

        return new_product

     except Exception as e:
        self.__conn.rollback()
        logger.exception("Error al intentar crear el producto")
        print(f"Error en create_product: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating product: {str(e)}",
        )
    
    def update_product(self, id: int, product: ProductUpdate):
        self.__conn.query(Product).filter(Product.id == id).update(product.dict())
        self.__conn.commit()
        return {"message": "Product updated successfully"}
    
    def delete_product(self, id: int):
        self.__conn.query(Product).filter(Product.id == id).delete()
        self.__conn.commit()
        return {"message": "Product deleted successfully"}    