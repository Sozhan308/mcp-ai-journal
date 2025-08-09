from app.main import app 

import pytest
import asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from datetime import datetime, timedelta

@pytest.mark.asyncio
async def test_health_endpoint(client):
        response = await client.get("/api/v1/health")
        assert response.status_code==200
        data = response.json()
        assert "version" in data
        assert isinstance(data['version'], str)
        assert "timestamp" in data
        ts = datetime.fromisoformat(data['timestamp'].replace("Z","+00:00"))
        assert isinstance(ts, datetime)
        assert ts.tzinfo is not None
        assert ts.utcoffset() == timedelta(0)
        
        assert "uptime" in data
        assert isinstance(data['uptime'], float)
        assert data['uptime'] > 0
        
        first_ts = datetime.fromisoformat(data['timestamp'].replace("Z", "+00:00"))
        first_uptime = data['uptime']
        
        await asyncio.sleep(0.01)
        
        response2 = await client.get("/api/v1/health")
        data2 = response2.json()
        
        second_ts = datetime.fromisoformat(data2['timestamp'].replace("Z", "+00:00"))
        second_uptime = data2['uptime']
        
        assert second_ts>=first_ts
        assert second_ts!=first_ts
        assert second_uptime>=first_uptime