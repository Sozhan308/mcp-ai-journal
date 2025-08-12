from app.schemas.user import UserCreationSchema
from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.post('/user',response_model=UserCreationSchema,summary="Creating user")


def create_user(user: UserCreationSchema) -> UserCreationSchema:
    return user
    # return UserCreationSchema(
    #     username="default",
    #     email="sozhan308@gmail.com",
    #     signup_ts=datetime.now(timezone.utc)
    # )