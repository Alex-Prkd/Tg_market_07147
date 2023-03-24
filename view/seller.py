from aiogram import types

from keyboards import InformationSeller, ButtonBackInformationSeller


# Информация для продавца
async def get_info_seller(callback_query: types.CallbackQuery):
    # Ознакомлен
    if callback_query.data == "contact_with_admin":
        await callback_query.message.answer(text=f"Связь с админом: @alex_prkd")

    else:
        """Не лучше ли импортировать клавиатуру в тот момент, когда она необходима,
        а не в начале файла?
        """
        btn_back = ButtonBackInformationSeller().button_back
        # Поиск информации по бд
        await callback_query.message.edit_text(text=f"Инофрмация {callback_query.data}",
                                               reply_markup=btn_back.as_markup())


async def get_my_shop(callback_query: types.CallbackQuery):
    info_seller = InformationSeller().keyboards
    """Если нет магазина в бд"""
    await callback_query.message.edit_text(text="У вас нет магазина. Для регистрации ознакомьтесь.",
                                           reply_markup=info_seller.as_markup())
    """Добавить меню, если если есть магазин"""


async def edit_photo(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass


async def edit_title(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass


async def edit_description(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass


async def edit_product(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass


async def edit_location(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass


async def add_admin(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass


async def delete_admin(callback_query: types.CallbackQuery):
    """Этот фунцкионал будет работать,
     когда подкину бд и создам магазин т.к. никуда реализовывать"""

    """Использовать FMS для работы"""
    pass

