from aiogram import types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

import config
from db.commands.reader import check_admin_bot, get_users, check_user
from db.commands.writer import change_role, set_photo_db, add_super_admin
from keyboards import AdminMenu, SelectRole, EditInfo, KeyboardBlacklist
from storage.EditBotInfo import AddSeller, EditInfoFSM, SuperAdmin


async def start_admin_menu(message: types.Message | types.CallbackQuery, session: AsyncSession) -> None:
    admin = await check_admin_bot(session, message)
    if admin is not None:
        """Главное меню админа"""
        """Калбэк необходим для возврата в главное меню из инлайн клавиатуры"""
        admin_keyboard = AdminMenu().admin_menu
        photo = config.BotPhoto.PHOTO
        try:
            # Из бд
            await message.answer_photo(photo=photo)
            await message.answer(f"Добро пожаловать {message.from_user.first_name}",
                                 reply_markup=admin_keyboard.as_markup())
        except AttributeError:
            await message.message.edit_text(text=f"Добро пожаловать {message.from_user.first_name}",
                                            reply_markup=admin_keyboard.as_markup())


async def add_seller(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(AddSeller.username_seller)
    await callback_query.message.answer(f"Введите никнейм продавца."
                                        f"\nПр.: {callback_query.from_user.username}")


async def edit_role_user(message: types.Message, session: AsyncSession, state: FSMContext):
    await state.clear()
    """Меняет роль пользователя с покупателя на продавца"""
    await change_role(session, message.text)


async def get_shops(callback_query: types.CallbackQuery):
    """Собирает все магазины"""
    """Добавить хэндер для выбора магазина"""
    await callback_query.message.answer(text="Собирает все магазины из бд и инфу о админе магазина")


# Поменять название
async def get_costumers(callback_query: types.CallbackQuery, session: AsyncSession):
    users = await get_users(session)
    for user in users:
        await callback_query.message.answer(text=f"username: @{user[0].username}\n"
                                                 f"role: {user[0].role}\n"
                                                 f"id: {user[0].id_telegram}")


async def select_role(callback_query: types.CallbackQuery):
    """Предлагает две роли (покупатель/продавец)
        роль передаётся в edit_info для генерации клавиатуры
    """
    btn_role = SelectRole().role
    await callback_query.message.edit_text(text="Изменить информацию",
                                           reply_markup=btn_role.as_markup())


async def edit_info(callback_query: types.CallbackQuery):
    btn_info = EditInfo(callback_query.data)
    await callback_query.message.edit_text(text="Выбор нужной графы для изменения",
                                           reply_markup=btn_info.edit.as_markup(resize_keyboard=True))


async def blacklist_menu(callback_query: types.CallbackQuery):
    blacklist_keyboard = KeyboardBlacklist()
    await callback_query.message.edit_text(text="ЧС",
                                           reply_markup=blacklist_keyboard.blacklist_k.as_markup())


async def edit_photo_main_menu(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(EditInfoFSM.photo_bot)
    await callback_query.message.answer("Пришлите фото:")


async def set_photo_bot(message: types.Message, session: AsyncSession, state: FSMContext) -> None:
    await state.clear()
    new_photo = message.photo[0].file_id
    await set_photo_db(session, new_photo)
    config.BotPhoto.PHOTO = new_photo


async def add_admin_bot(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(SuperAdmin.username)
    await callback_query.message.answer("Введите id профиля, для того чтобы сделать его админом.")


async def get_username_new_admin(message: types.Message, session: AsyncSession, state: FSMContext):
    await state.clear()
    user = await check_user(session, message.text, message.from_user.username)
    if user is None:
        await message.answer(text=f"Проверьте вводимые данные.")
    else:
        await add_super_admin(session, message.text)
        await message.answer(text=f"Пользователь добавлен")