from aiogram import types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from db.commands.writer import add_info_about_seller, add_instruction_seller, add_regulations_seller
from storage.EditBotInfo import EditInfoFSM


async def edit_about_seller(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(EditInfoFSM.about_seller)
    await callback_query.message.answer(text="Напишите текст \"Почему мы?\" (для продавца).")


async def get_info_about_seller(message: types.Message, session: AsyncSession):
    await add_info_about_seller(session_maker=session, message=message)


async def edit_instruction_seller(callback_query: types.CallbackQuery, state: FSMContext):
    print("INSTRUCTION!!!!!!!!")
    print(callback_query.data)
    await state.set_state(EditInfoFSM.instruction_seller)
    await callback_query.message.answer(text="Напишите текст \"Инструкция?\" (для продавца).")


async def get_instruction_seller(message: types.Message, session: AsyncSession):
    await add_instruction_seller(session, message)


async def edit_regulations_seller(callback_query: types.CallbackQuery, state: FSMContext):
    print("REGULATIONS!!!!!!!!")
    print(callback_query.data)
    await state.set_state(EditInfoFSM.regulations_seller)
    await callback_query.message.answer(text="Напишите текст \"Правил?\" (для продавца).")


async def get_regulations_seller(message: types.Message, session: AsyncSession):
    await add_regulations_seller(session, message)