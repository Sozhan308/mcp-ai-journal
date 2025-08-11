from app.schemas.config import ConfigResponse
from fastapi import APIRouter, Depends, Request
from datetime import datetime, timezone

router = APIRouter(tags=["config"])

def get_settings(request: Request):
    return request.app.state.settings

def get_uptime(request: Request) -> float:
    return (datetime.now(timezone.utc) - request.app.state.start_time).total_seconds() 

def get_config(settings = Depends(get_settings)) -> ConfigResponse: 
    return ConfigResponse(
    app_name=settings.app_name,
    version=settings.version,
    debug=settings.debug
    )
    
@router.get("/config",response_model=ConfigResponse, summary="return app config information")   
def read_config(cfg : ConfigResponse = Depends(get_config)) -> ConfigResponse:
    return cfg