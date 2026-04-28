from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from helpers.db import get_db
from services import OAuthError, OAuthService
from adapters import GoogleAPIError

class OAuthController:
    def __init__(self, oauth_service: OAuthService, redirect_url: str):
        self.oauth_service = oauth_service
        self.redirect_url = redirect_url

    def register_routes(self, app: FastAPI):

        @app.get("/api/v1/auth/callback/google")
        async def oauth_google(request: Request, _: Response, db: AsyncSession = Depends(get_db)):
            try:
                code = request.query_params.get("code")
                if not code:
                    return JSONResponse(status_code=400, content={"message": "Authorization code not provided"})
                token = await self.oauth_service.google_oauth(db, code)
                res = RedirectResponse(url=self.redirect_url, status_code=302)
                res.set_cookie(
                    key="sid",
                    value=token,
                    httponly=True,
                    samesite="none",
                    secure=True,
                    max_age=60*60*24*30,
                    path="/",
                )
                return res
            except OAuthError as e:
                return JSONResponse(status_code=e.status_code, content={"message": e.message})
            except GoogleAPIError as e:
                return JSONResponse(status_code=e.status_code, content={"message": e.message})
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": str(e)})