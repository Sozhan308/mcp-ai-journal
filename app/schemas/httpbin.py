from pydantic import BaseModel
from datetime import datetime, timezone

class HttpBinResponse(BaseModel):
    url: str
    origin: str
    user_agent: str
    fetched_at: datetime
    
    