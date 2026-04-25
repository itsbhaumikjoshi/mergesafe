import os
import bcrypt
from .jwt_service import JWTService
from repositories import UserRepo
from sqlalchemy.ext.asyncio import AsyncSession

class AuthError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class AuthService:
    def __init__(self):
        secret = os.getenv("JWT_SECRET", "supersecret")
        self.jwt_service = JWTService(secret)

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    async def login(self, db: AsyncSession, email: str, password: str) -> str:
        repo = UserRepo(db)
        user = await repo.find_by_email(email)
        
        if not user or not self.verify_password(password, user.password):
            raise AuthError("Invalid email or password", 401)
        
        return self.jwt_service.sign({"id": str(user.id)})

    async def register(self, db: AsyncSession, user_data: dict) -> str:
        repo = UserRepo(db)
        email = user_data["email"]
        
        if await repo.exists_by_email(email):
            raise AuthError("User already exists", 409)
        
        user_data["password"] = self.hash_password(user_data["password"])

        user = await repo.create_user(user_data)
        
        return self.jwt_service.sign({"id": str(user.id)})

    async def get_current_user(self, db: AsyncSession, token: str):
        try:
            payload = self.jwt_service.verify(token)
            id = payload.get("id")
            if not id:
                return None
            repo = UserRepo(db)
            return await repo.find_by_id(id)
        except Exception:
            return None
