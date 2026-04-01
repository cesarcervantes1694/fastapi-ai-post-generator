
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from starlette.middleware.base import BaseHTTPMiddleware
from settings.config import ALGORITHM, SECRET_KEY

class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        
        if request.url.path in ["/login"]:
            return await call_next(request)
        
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JSONResponse(
                status_code=401,
                content={"detail": "Token requerido"}
            )

        # Error
        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.state.user = payload.get("sub")
        except JWTError:
            # raise HTTPException(status_code=401, detail="Token inválido")
            return JSONResponse(
                status_code=401,
                content={"detail": "Token requerido 2"}
            )

        return await call_next(request)


