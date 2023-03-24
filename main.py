import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from view import start_commands, menu_costumer, menu_seller, menu_admin


async def main() -> None:
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot("5561473793:AAGc4-ZSGh8XCBzAI0DVGcWxLHCVFpmwwkM", parse_mode="HTML")
    start_commands(dp)
    menu_costumer(dp)
    menu_seller(dp)
    menu_admin(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())