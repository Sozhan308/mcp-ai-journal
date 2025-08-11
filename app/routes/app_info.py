from app.schemas.app_info import AppInfoResponse
from app.routes.config import get_settings, get_uptime
from fastapi import APIRouter, Depends
import sys, platform
from datetime import datetime, timezone

router = APIRouter()

@router.get("/app-info", response_model=AppInfoResponse, summary="Return runtime/appserver information")

def server_info(settings = Depends(get_settings), uptime = Depends(get_uptime)) -> AppInfoResponse:
    return AppInfoResponse(
        app_name=settings.app_name,
        version=settings.version,
        uptime=uptime
    )