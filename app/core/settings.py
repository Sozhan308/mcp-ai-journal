from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "MCP Learning AI"
    version: str= "0.1.0"
    debug: bool= True