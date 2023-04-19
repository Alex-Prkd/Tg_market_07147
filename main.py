import asyncio


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import select

import config
from db import get_session_maker, create_engine, AdminBot
from middlewares import DbSessionMiddleware
from middlewares.check_blacklist import CheckUserInBlacklist
from middlewares.check_userDB import CheckUser
from view import start_commands, menu_costumer, menu_seller, menu_admin, edit_info_bot, menu_blacklist


async def main() -> None:
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.BotConfig.TOKEN, parse_mode="HTML")

    start_commands(dp)
    menu_costumer(dp)
    menu_seller(dp)
    menu_admin(dp)
    edit_info_bot(dp)
    menu_blacklist(dp)

    engine = create_engine(config.BotConfig.DATABASE_URI)
    session_maker = get_session_maker(engine)


    async with session_maker() as session:
        print('\n', "set photo in config\n")
        result = await session.scalar(select(AdminBot))
        config.BotPhoto.PHOTO = result.photo_bot


    dp.message.middleware(DbSessionMiddleware(session_maker))
    dp.callback_query.middleware(DbSessionMiddleware(session_maker))
    dp.message.middleware(CheckUser(session_maker))
    dp.message.middleware(CheckUserInBlacklist(session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())