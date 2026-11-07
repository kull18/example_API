from fastapi import Request
from fastapi import Form
from fastapi import APIRouter
from src.features.products.infraestructure.controllers.ProductController import ProductController
from src.features.products.domain.schemas.ProductSchema import ProductCreate, ProductUpdate
from fastapi import UploadFile, File
from src.features.products.application.dto.ProductResponseDTO import ProductResponseDTO

router = APIRouter()

product_controller = ProductController()

@router.get("/products")
async def get_all_products():
    return product_controller.get_all_products()

@router.get("/products/{id}")
async def get_product_by_id(id: int):
    return product_controller.get_product_by_id(id)

@router.post("/products", response_model=ProductResponseDTO)
async def create_product(
    request: Request,
    name: str = Form(..., min_length=3, max_length=100),
    price: float = Form(..., gt=0),
    description: str = Form(..., min_length=10, max_length=1000),
    image: UploadFile = File(...)
):
    return await product_controller.create_product(
        request,
        name=name,
        price=price,
        description=description,
        image=image
    )

@router.put("/products/{id}")
async def update_product(id: int, product: ProductUpdate):
    return product_controller.update_product(id, product)

@router.delete("/products/{id}")
async def delete_product(id: int):
    return product_controller.delete_product(id)    