import sqlalchemy.exc
from aiogram.types import Message
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from db import User, AdminBot, Description
from db.models import Blacklist


async def add_user(session_maker: AsyncSession, data: Message):
    """При старте бота добавляет нового пользователя"""
    print("ADD USER")
    user = User()
    user.id_telegram = data.from_user.id
    user.username = data.from_user.username
    session_maker.add(user)
    await session_maker.commit()


async def set_photo_db(session_maker: AsyncSession, new_photo):
    """
    Админ меню - изменить фото главного меню.
    Добавляет в бд, в файле main забирает из бд,
    присваевает в config.BotPhoto.PHOTO
    """
    async with session_maker as session:
        result = await session.scalar(select(AdminBot))
        result.photo_bot = new_photo
        await session.commit()


async def change_role(session_maker: AsyncSession, username):
    """
    Админ меню (Добавить продавца)
    Изменяет role пользователя.
    costumer -> seller
    """
    async with session_maker as session:
        stmt = select(User).where(User.username == username)
        result = await session.scalar(stmt)
        print(result)
        if result is not None:
            result.role = "seller"
            await session.commit()


# не получается первый раз прокинуть сессию т.к. нет данных -> try: except:
async def add_info_about_seller(session_maker: AsyncSession, message: Message):
    print(f"\n ADD INFO ABOUT SELLER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        result.about_seller = message.text
        await session.commit()


async def add_instruction_seller(session_maker: AsyncSession, message: Message):
    print(f"\n ADD INSTRUCTION SELLER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        result.instruction_seller = message.text
        await session.commit()


async def add_regulations_seller(session_maker: AsyncSession, message: Message):
    print(f"\n ADD INSTRUCTION SELLER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        result.regulations_seller = message.text
        await session.commit()


""""""


async def add_info_about_costumer(session_maker: AsyncSession, message: Message):
    print(f"\n ADD INFO ABOUT COSTUMER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        result.about_costumer = message.text
        await session.commit()


async def add_instruction_costumer(session_maker: AsyncSession, message: Message):
    print(f"\n ADD INSTRUCTION COSTUMER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        result.instruction_costumer = message.text
        await session.commit()


async def add_regulations_costumer(session_maker: AsyncSession, message: Message):
    print(f"\n ADD INSTRUCTION COSTUMER")
    async with session_maker as session:
        result = await session.scalar(select(Description))
        result.regulations_costumer = message.text
        await session.commit()


""""""


async def add_user_blacklist(session_maker: AsyncSession, username: str):
    async with session_maker as session:
        user = await session.scalar(select(User).where(User.username == username))
        try:
            if user is not None:
                """Профиль найден в бд"""
                user_blacklist = Blacklist()
                user_blacklist.id_telegram = user.id_telegram
                user_blacklist.username = user.username
                user_blacklist.role = user.role
                session.add(user_blacklist)
                await session.commit()
                return True
        except sqlalchemy.exc.IntegrityError:
            """Исключение если уже есть в чс"""
            pass
        """Профиль не найден, сообщение админу"""
        return False


async def delete_from_blacklist(session_maker: AsyncSession, username: str):
    async with session_maker as session:
        user_blacklist = await session.scalar(select(Blacklist).where(Blacklist.username == username))
        if user_blacklist is not None:
            """Профиль найден в бд"""
            stmt = delete(Blacklist).where(Blacklist.username == username)
            await session.execute(stmt)
            await session.commit()
            return True
        """Профиль не найден, сообщение админу"""
        return False


async def add_super_admin(session_maker: AsyncSession, id):
    async with session_maker as session:
        try:
            """Добавляем в админы"""
            new_admin = AdminBot()
            new_admin.id_telegram = int(id)
            session.add(new_admin)
            await session.commit()
        except sqlalchemy.exc.IntegrityError:
            """Если в бд уже есть """
            return