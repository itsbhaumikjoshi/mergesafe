from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_email(self, email: str) -> User | None:
        result = await self.session.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def find_by_id(self, user_id: UUID) -> User | None:
        result = await self.session.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def create_user(self, user_data: dict) -> User:
        user = User(
            email=user_data["email"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"]
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def exists_by_email(self, email: str) -> bool:
        user = await self.find_by_email(email)
        return user is not None
