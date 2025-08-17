from app.schemas.httpbin import HttpBinResponse
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timezone
import httpx

def get_http_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(timeout=5.0)

router = APIRouter(tags=["External"])

@router.get('/external-httpbin', response_model=HttpBinResponse)

async def external_httpbin(client: httpx.AsyncClient= Depends(get_http_client)) -> HttpBinResponse:
    try:
        response = await client.get("http://httpbin.org/get")
        response.raise_for_status()
        data = response.json()
        return HttpBinResponse(
            url = data['url'],
            origin=data.get("origin", ""),
            user_agent=data['headers']['User-Agent'], # data.get("headers", {}).get("User-Agent","")
            fetched_at=datetime.now(timezone.utc)
        )
    except (httpx.HTTPStatusError, httpx.RequestError) as e:
        raise HTTPException(           
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Upstream error contacting httpbin: {e.__class__.__name__}"
        )
    finally:
        await client.aclose()

