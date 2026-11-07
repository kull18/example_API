from src.features.users.application.dto.UserResponseDTO import UserResponseDTO
from src.features.users.domain.models import UserModel

def to_user_response(user: UserModel) -> UserResponseDTO:
    return UserResponseDTO(
        user_id=user.user_id,
        username=user.username,
        email=user.email
    )