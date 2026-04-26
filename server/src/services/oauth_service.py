from sqlalchemy.ext.asyncio import AsyncSession

from repositories import UserRepo
from .jwt_service import JWTService
from adapters import GoogleOAuthAPI

class OAuthError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class OAuthService:
    def __init__(self, jwt_service: JWTService, google_oauth_api: GoogleOAuthAPI):
        self.jwt_service = jwt_service
        self.google_oauth_api = google_oauth_api

    async def google_oauth(self, db: AsyncSession, code: str):
        user_data = await self.google_oauth_api.fetch_user_info(code)

        repo = UserRepo(db)
        db_user = await repo.find_by_email(user_data.get("email"))
        if not db_user:
            db_user = await repo.create_user(user_data)
        
        return self.jwt_service.sign({"id": str(db_user.id)})
