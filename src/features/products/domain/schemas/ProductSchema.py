from pydantic import BaseModel, Field


class BaseProduct(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    price: float = Field(..., gt=0)
    description: str = Field(..., min_length=10, max_length=1000)

    model_config = {
        "from_attributes": True
    }


class ProductCreate(BaseProduct):
    pass


class ProductUpdate(BaseProduct):
    pass


class ProductResponse(BaseProduct):
    id: int
    created_at: str
    updated_at: str