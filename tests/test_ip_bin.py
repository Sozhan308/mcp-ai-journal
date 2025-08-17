from app.main import app

from app.schemas.ipbin import IPResponse
from app.routes.ipbin import get_http_client

import pytest
import asyncio

class FakeResponse:
    def __init__(self, status_code:int, payload: dict):
        self.status_code = status_code
        self.payload = payload
    
    def json(self):
        return self.payload

class FakeClient:
    def __init__(self, status_code:int=200):
        self.status_code = status_code
    async def get(self, origin:str):
        # return dummmy IP
        payload = {"origin": "127.0.0.1"}
        status_code = self.status_code
        return FakeResponse(payload=payload, status_code=status_code)
    async def aclose(self):
        pass

@pytest.mark.asyncio

async def test_ip_endpoint(client):
    app.dependency_overrides[get_http_client] = lambda: FakeClient()
    response = await client.get("/api/v1/external-ip")
    assert response.status_code == 200
    data = response.json()
    assert data['origin'] == "127.0.0.1"
    app.dependency_overrides.clear()