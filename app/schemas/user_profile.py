from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserProfileSchema(BaseModel):
    username: str= Field(..., min_length=5)
    email: EmailStr
    age: int= Field(..., le=60, ge=18)
    bio: Optional[str]= Field(None, max_length=200)