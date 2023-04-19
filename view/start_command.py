
from aiogram import types

import config
from keyboards import MainMenu


async def command_start_menu(message: types.Message | types.CallbackQuery):
    keyboards_start = MainMenu().keyboards_start
    photo = config.BotPhoto.PHOTO
    try:
        await message.answer_photo(photo=photo)
        await message.answer(text="Главное меню",
                             reply_markup=keyboards_start.as_markup(resize_markup=True))
    except AttributeError:
        message: types.CallbackQuery
        await message.message.edit_text(text="Главное меню",
                                        reply_markup=keyboards_start.as_markup())
