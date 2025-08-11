from pydantic import BaseModel 
from datetime import datetime

class AppInfoResponse(BaseModel):
    app_name: str
    version: str
    uptime: float