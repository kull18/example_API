from pydantic import BaseModel

class UserBaseModel(BaseModel):
    username: str
    password: str
    email: str

    model_config = {
        "from_attributes": True
    }

class CreateUser(UserBaseModel):
    pass

class UpdateUser(UserBaseModel):
    pass

class ResponseUser(UserBaseModel):
    user_id: int
    created_at: str
    updated_at: str

class LoginModel(BaseModel):
    email: str
    password: str

class ChangePasswordModel(BaseModel):
    password: str
    new_password: str