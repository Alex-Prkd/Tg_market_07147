from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from sqlalchemy.orm import sessionmaker

from db.commands.reader import check_user
from db.commands.writer import add_user


class CheckUser(BaseMiddleware):
    print("CHECKUSER\n")
    def __init__(self, session: sessionmaker):
        self.session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user = await check_user(session_maker=self.session(),
                                id=event.from_user.id,
                                username=event.from_user.username)
        if user is None:
            await add_user(session_maker=self.session(),
                           data=event)
        return await handler(event, data)

