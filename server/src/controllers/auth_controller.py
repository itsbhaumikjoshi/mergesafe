from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from helpers.db import get_db, AsyncSessionLocal
from services import AuthService, AuthError

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class AuthController:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def register_routes(self, app: FastAPI):
        
        @app.middleware("http")
        async def auth_middleware(request: Request, call_next):
            request.state.user = None
            sid = request.cookies.get("sid")
            if sid:
                async with AsyncSessionLocal() as session:
                    user = await self.auth_service.get_current_user(session, sid)
                    if user:
                        request.state.user = user
            
            response = await call_next(request)
            return response

        @app.post("/api/v1/auth/login")
        async def login(data: LoginRequest, response: Response, db: AsyncSession = Depends(get_db)):
            try:
                token = await self.auth_service.login(db, data.email, data.password)
                response.set_cookie(key="sid", value=token, httponly=True, samesite="none", secure=True, max_age=60*60*24*30)
            except AuthError as e:
                return JSONResponse(status_code=e.status_code, content={"message": e.message})
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": str(e)})

        @app.post("/api/v1/auth/register")
        async def register(data: RegisterRequest, response: Response, db: AsyncSession = Depends(get_db)):
            try:
                token = await self.auth_service.register(db, data.model_dump())
                response.set_cookie(key="sid", value=token, httponly=True, samesite="none", secure=True, max_age=60*60*24*30)
            except AuthError as e:
                return JSONResponse(status_code=e.status_code, content={"message": e.message})
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": str(e)})

        @app.post("/api/v1/auth/logout")
        async def logout(response: Response):
            response.delete_cookie(key="sid")

        @app.get("/api/v1/auth/me")
        async def get_me(request: Request):
            user = request.state.user
            if not user:
                return JSONResponse(status_code=401, content={"message": "Unauthorized"})
            return {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }
