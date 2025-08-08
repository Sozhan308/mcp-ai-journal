from fastapi import FastAPI
from datetime import datetime, timezone

from app.routes.health import router as health_router

app = FastAPI()

app.state.start_time = datetime.now(timezone.utc)

app.include_router(health_router)