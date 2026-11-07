from src.features.products.application.dto.ProductResponseDTO import ProductResponseDTO
from src.features.products.domain.models.ProductModel import Product
from pathlib import Path
from fastapi import Request

def to_product_response(product: Product, request: Request) -> ProductResponseDTO:
    filename = Path(product.image).name
    base_url = str(request.base_url).rstrip("/")
    full_image_url = f"{base_url}/static/products/{filename}"

    return ProductResponseDTO(
        id=product.id,
        name=product.name,
        price=product.price,
        description=product.description,
        image=full_image_url,
    )