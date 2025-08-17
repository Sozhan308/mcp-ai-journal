from app.schemas.user_profile import UserProfileSchema
from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.post("/profile", response_model=UserProfileSchema, summary="User Profile information")

def user_profile(profile: UserProfileSchema) -> UserProfileSchema:
    return profile