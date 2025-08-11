from app.main import app 

from app.core.settings import Settings
from app.routes.config import get_settings
import pytest
import asyncio
from datetime import datetime, timedelta

def fake_get_config_settings():
    return Settings(
        app_name="Test App",
        version="X.Y.Z"
    )

@pytest.mark.asyncio

async def test_app_info_endpoint(client):
        app.dependency_overrides[get_settings] = fake_get_config_settings
        response = await client.get("/api/v1/app-info")
        assert response.status_code == 200
        data = response.json()
        assert "app_name" in data
        assert isinstance(data['app_name'], str)
        assert "version" in data
        assert data['version'] == 'X.Y.Z'
        assert isinstance(data['uptime'], float)
