from aiogram import types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from db.commands.reader import users_blacklist
from db.commands.writer import add_user_blacklist, delete_from_blacklist
from storage.EditBotInfo import AddUserToBlacklist, DeleteUserToBlacklist


async def all_blacklist(callback_query: types.CallbackQuery, session: AsyncSession):
    users = await users_blacklist(session)
    if users is not False:
        """В чс есть прользователи"""
        for user in users:
            await callback_query.message.answer(text=f"username: @{user[0].username}\n"
                                                     f"id: {user[0].id_telegram}\n"
                                                     f"role: {user[0].role}")
    else:
        """В чс нет пользователей"""
        await callback_query.message.answer(text=f"Чёрный список пуст.")



async def add_blacklist(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(AddUserToBlacklist.username)
    await callback_query.message.answer("Введите username профиля, и он уйдёт в чс.")


async def get_username_for_blacklist(message: types.Message, session: AsyncSession):
    result = await add_user_blacklist(session, message.text)
    if result:
        await message.answer(text=f"Пользователь @{message.text} добавлен в ЧС.")
    else:
        await message.answer(text=f"Пользователь @{message.text} не найден в базе.")


async def delete_blacklist(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(DeleteUserToBlacklist.username)
    await callback_query.message.answer("Введите username профиля для того, чтобы убрать его из ЧС.")


async def get_username_for_delete_blacklist(message: types.Message, session: AsyncSession):
    result = await delete_from_blacklist(session, message.text)
    if result:
        await message.answer(text=f"Пользователь убран @{message.text} из ЧС.")
    else:
        await message.answer(text=f"Пользователь @{message.text} не найден в базе.")