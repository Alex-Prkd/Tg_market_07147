from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import User, AdminBot, Description
from db.models import Blacklist


async def check_user(session_maker: AsyncSession, id, username):
    """Фунцкия вызывается, при возврате в middleware"""
    async with session_maker as session:
        user = await session.get(User, id)
        if user is not None and user.username != username:
            """Проверка на изменение username, если не совпадает обновляется """
            user.username = username
            await session.commit()
    return user


async def check_user_in_blacklist(session_maker: AsyncSession, id):
    """Проверка нет пользователя в ЧС.
        Вызывается в middleware
    """
    async with session_maker as session:
        user = await session.get(Blacklist, id)
        return user



async def check_admin_bot(session_maker: AsyncSession, data: Message):
    async with session_maker as session:
        stmt = select(AdminBot).where(AdminBot.id_telegram == data.from_user.id)
        result = await session.execute(stmt)
        user = result.first()
    return user


async def get_users(session_maker: AsyncSession):
    async with session_maker as session:
        result = await session.execute(select(User))
    return result.all()


async def users_blacklist(session_maker: AsyncSession):
    async with session_maker as session:
        result = await session.execute(select(Blacklist))
        users = result.all()
        print()
        print(users)
        """Список ЧС пустой."""
        if len(users) < 1:
            return False
    return users


async def get_information_for_seller(session_maker: AsyncSession, data: str):
    print("RESPONSE INFO SELLER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        print(result.first())