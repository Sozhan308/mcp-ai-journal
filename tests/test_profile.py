from app.main import app 

import pytest
import asyncio
from datetime import datetime, timedelta
from app.schemas.user_profile import UserProfileSchema

@pytest.mark.asyncio

async def test_profile_valid_client(client):
    payload = {"username":"sozhan_dev", "email":"abc@gmail.com", "age":28}
    response = await client.post("/api/v1/profile", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "username" in data
    assert len(data['username']) > 2
    assert "email" in data
    assert isinstance(data['email'], str)

async def test_profile_invalid_client(client):
    payload = {"username":"abcddfdf", "email":"abcemail.com", "age":90}
    response = await client.post("/api/v1/profile", json=payload)
    assert response.status_code == 422
    data = response.json()
    