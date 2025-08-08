from datetime import datetime, timezone
from app.schemas.health import HealthResponse
from fastapi import APIRouter, Request


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check(request:Request) -> HealthResponse:
    return HealthResponse(
        version='0.1.0',
        timestamp=datetime.now(timezone.utc),
        uptime=(datetime.now(timezone.utc)- request.app.state.start_time).total_seconds()
    )