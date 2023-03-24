from aiogram import types


from keyboards import ADMIN_ID, AdminMenu
from keyboards.admin import SelectRole, EditInfo


async def start_admin_menu(message: types.Message | types.CallbackQuery) -> None:
    if message.from_user.id == ADMIN_ID:
        """Главное меню админа"""
        """Калбэк необходим для возврата в главное меню из инлайн клавиатуры"""
        admin_keyboard = AdminMenu().admin_menu
        try:
            await message.answer_photo(photo="AgACAgIAAxkBAAITtmQT0_aNtfTLlluxLZgMOyBZognTAALXwzEb_W2gSIK-252iJM_lAQADAgADcwADLwQ")
            await message.answer(f"Добро пожаловать {message.from_user.first_name}",
                                 reply_markup=admin_keyboard.as_markup())
        except AttributeError:
            await message.message.edit_text(text=f"Добро пожаловать {message.from_user.first_name}",
                                            reply_markup=admin_keyboard.as_markup())
    else:
        pass


async def get_shops(callback_query: types.CallbackQuery):
        """Собирает все магазины"""
        """Добавить хэндер для выбора магазина"""
        await callback_query.message.answer(text="Собирает все магазины из бд и инфу о админе магазина")


async def get_costumers(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="Список всех пользователей в боте")


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


async def blacklist(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="ЧС")


async def add_seller(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Добавить продавца")
