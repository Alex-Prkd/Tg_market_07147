from aiogram import types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from db.commands.writer import add_info_about_costumer, add_instruction_costumer, add_regulations_costumer
from storage.EditBotInfo import EditInfoFSM


async def edit_about_costumer(callback_query: types.CallbackQuery, state: FSMContext):
    print("ABOUT COSTUMER!!!!!!!")
    await state.set_state(EditInfoFSM.about_costumer)
    await callback_query.message.answer(text="Напишите текст \"Почему мы?\" (для покупателя).")


async def get_info_about_costumer(message: types.Message, session: AsyncSession):
    await add_info_about_costumer(session_maker=session, message=message)


async def edit_instruction_costumer(callback_query: types.CallbackQuery, state: FSMContext):
    print("INSTRUCTION COSTUMER!!!!!!!!")
    print(callback_query.data)
    await state.set_state(EditInfoFSM.instruction_costumer)
    await callback_query.message.answer(text="Напишите текст \"Инструкция?\" (для покупателя).")


async def get_instruction_costumer(message: types.Message, session: AsyncSession):
    await add_instruction_costumer(session, message)


async def edit_regulations_costumer(callback_query: types.CallbackQuery, state: FSMContext):
    print("REGULATIONS COSTUMER!!!!!!!!")
    await state.set_state(EditInfoFSM.regulations_costumer)
    await callback_query.message.answer(text="Напишите текст \"Правил?\" (для покупателя).")


async def get_regulations_costumer(message: types.Message, session: AsyncSession):
    await add_regulations_costumer(session, message)