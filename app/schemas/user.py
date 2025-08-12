from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, timezone

class UserCreationSchema(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    signup_ts: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))