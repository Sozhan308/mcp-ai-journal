from pydantic import BaseModel 
from datetime import datetime

class ServerInfoResponse(BaseModel):
    server_name: str
    python_version: str
    platform: str
    timestamp: datetime