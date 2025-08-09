from fastapi import FastAPI
from datetime import datetime, timezone

from app.routes.health import router as health_router
from app.routes.server_info import router as server_router

APP_VERSION = "0.1.0"

app = FastAPI(title="MCP Learning", version=APP_VERSION)

app.state.start_time = datetime.now(timezone.utc)

API_PREFIX = "/api/v1"

app.include_router(health_router, prefix=API_PREFIX)
app.include_router(server_router, prefix=API_PREFIX)