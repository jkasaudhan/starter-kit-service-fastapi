from fastapi import Header, HTTPException, status
from app.core.config import settings

async def get_token_header(x_token: str = Header(...)):
    if x_token != settings.SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )