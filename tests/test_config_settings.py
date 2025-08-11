from app.main import app
from app.routes.config import get_settings
from app.schemas.config import ConfigResponse
from app.core.settings import Settings

import pytest
import asyncio

def fake_get_config_settings():
    return Settings(
        app_name="Test Settings with App",
        version="7.7.7",
        debug=False
    )

@pytest.mark.asyncio

async def test_config_endpoint(client):
    app.dependency_overrides[get_settings] = fake_get_config_settings
    response = await client.get("/api/v1/config")
    assert response.status_code==200
    data = response.json()
    assert data['debug'] is False
    assert data['version'] == '7.7.7'
    assert "Test Settings with App" in data['app_name']
    app.dependency_overrides.clear()