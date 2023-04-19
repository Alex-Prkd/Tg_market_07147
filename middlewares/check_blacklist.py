from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from sqlalchemy.orm import sessionmaker

from db.commands.reader import check_user_in_blacklist


class CheckUserInBlacklist(BaseMiddleware):
    print("CHECKBLACKLIST")
    def __init__(self, session: sessionmaker):
        self.session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user = await check_user_in_blacklist(session_maker=self.session(),
                                             id=event.from_user.id)
        if user is None:
            return await handler(event, data)
        return event.answer(f"Вы в чёрном списке.")

