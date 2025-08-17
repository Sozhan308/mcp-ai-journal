from app.schemas.ipbin import IPResponse
from fastapi import APIRouter, Depends
from app.routes.httpbin import get_http_client
import httpx

router = APIRouter(tags=["External"])

@router.get("/external-ip", response_model=IPResponse)

async def external_ip(client: httpx.AsyncClient = Depends(get_http_client)) -> IPResponse:
    try:
        response = await client.get("https://httpbin.org/get")
        data = response.json()
        return IPResponse(
            origin=data.get("origin", "")
        )
    finally:
        await client.aclose()