from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ProductResponseDTO(BaseModel):
    id: int
    name: str
    price: float
    description: str
    image: str

    model_config = ConfigDict(from_attributes=True)