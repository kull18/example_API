from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserResponseDTO(BaseModel):
    user_id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)