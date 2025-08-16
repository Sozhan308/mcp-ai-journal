from app.main import app 

import pytest
import asyncio
from datetime import datetime, timedelta

@pytest.mark.asyncio

async def test_user_valid_client(client):
        payload = {"username":"abc", "email":"abc@gmail.com"}
        response = await client.post("/api/v1/user", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "username" in data
        assert len(data['username']) > 2
        assert "email" in data
        assert isinstance(data['email'], str)
        assert "signup_ts" in data

async def test_user_invalid_client(client):
    payload = {"username":"ab", "email":"abc@gmail.com"}
    response = await client.post("/api/v1/user", json=payload)
    assert response.status_code == 422
    data = response.json()
    