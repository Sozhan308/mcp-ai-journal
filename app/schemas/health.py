from pydantic import BaseModel 
from datetime import datetime

class HealthResponse(BaseModel):
    version: str
    timestamp: datetime
    uptime: float