from app.main import app
from app.routes.config import get_config
from app.schemas.config import ConfigResponse

import pytest
import asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from datetime import datetime, timedelta

def fake_get_config():
    return ConfigResponse(
        app_name="Test App",
        version="9.9.9",
        debug=False
    )

@pytest.mark.asyncio

async def test_config_endpoint(client):
    app.dependency_overrides[get_config] = fake_get_config
    response = await client.get("/api/v1/config")
    assert response.status_code==200
    data = response.json()
    assert data['debug'] is False
    assert "Test App" in data['app_name']
    app.dependency_overrides.clear()