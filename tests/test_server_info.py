from app.main import app 

import pytest
import asyncio
from datetime import datetime, timedelta

@pytest.mark.asyncio

async def test_server_info_endpoint(client):
        response = await client.get("/api/v1/server-info")
        assert response.status_code == 200
        data = response.json()
        assert "server_name" in data
        assert isinstance(data['server_name'], str)
        assert "python_version" in data
        assert "." in data['python_version']
        assert "platform" in data
        assert data['platform']
        assert "timestamp" in data
        ts = datetime.fromisoformat(data['timestamp'].replace("Z","+00:00"))
        assert isinstance(ts,datetime)
        assert ts.tzinfo is not None
        assert ts.utcoffset() == timedelta(0)
