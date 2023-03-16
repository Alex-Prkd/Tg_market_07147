from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from ..models import User


async def add_user(session: AsyncSession, user):
    print("add_user")
    print(user, "/n")
    user = User()
    user.username = ...
    user.telegram_id = ...

    session.add(user)
    await session.commit()


