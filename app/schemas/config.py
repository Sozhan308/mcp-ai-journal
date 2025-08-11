from pydantic import BaseModel 

class ConfigResponse(BaseModel):
    app_name: str
    version: str
    debug: bool