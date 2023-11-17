from fastapi import HTTPException
from fastapi.security import HTTPBearer
from starlette.requests import Request
from service.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if auth:
            validate_token(auth.credentials)
            data = validate_token(auth.credentials)
            if data["email"] != "admin@gmail.com":
                raise HTTPException(status_code=403, detail="Invalid Credentials")
