from app.main import app
from app.schemas.httpbin import HttpBinResponse
from app.routes.httpbin import get_http_client
from datetime import datetime, timezone

import pytest
import asyncio

class FakeResp:
    def __init__(self, payload: dict, status_code: int = 200):
        self._payload = payload
        self.status_code = status_code
    def json(self):
        return self._payload
    def raise_for_status(self):
        # simulate 4xx/5xx
        import httpx 
        if self.status_code >400:
            raise httpx.HTTPStatusError(message=f"Error: {self.status_code}", request=None, response=None)
    

class FakeClient:
    def __init__(self, status_code: int = 200):
        self.status_code = status_code
    async def get(self, url: str):
        # return a minimal shape like httpbin does
        payload = ({
            "url": "https://httpbin.org/get",
            "origin": "203.0.113.42",
            "headers": {"User-Agent": "pytest-fake"},
            "args": {}
        })
        return FakeResp(payload=payload, status_code=self.status_code)
    
    async def aclose(self):
        pass
    

@pytest.mark.asyncio

async def test_http_endpoint(client):
    app.dependency_overrides[get_http_client] = lambda: FakeClient(status_code=200)
    response = await client.get("/api/v1/external-httpbin")
    assert response.status_code==200
    data = response.json()
    assert data["url"] == "https://httpbin.org/get"
    assert data["origin"] == "203.0.113.42"
    assert data["user_agent"] == "pytest-fake"
    app.dependency_overrides.clear()
    
async def test_httpbin_upstream_error(client):
    app.dependency_overrides[get_http_client] = lambda: FakeClient(status_code=500)

    response = await client.get("/api/v1/external-httpbin")
    assert response.status_code == 502
    data = response.json()
    assert "Upstream error" in data["detail"]

    app.dependency_overrides.clear()