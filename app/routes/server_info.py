from app.schemas.server_info import ServerInfoResponse
from fastapi import APIRouter
import sys, platform
from datetime import datetime, timezone

router = APIRouter()

@router.get("/server-info", response_model=ServerInfoResponse, summary="Return runtime/server information")

def server_info() -> ServerInfoResponse:
    return ServerInfoResponse(
        server_name="MCP Learning API",
        python_version=sys.version,
        platform=platform.system(),
        timestamp=datetime.now(timezone.utc)
    )