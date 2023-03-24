
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton



async def command_start_menu(message: types.Message | types.CallbackQuery):
    keyboards_start = InlineKeyboardBuilder()
    keyboards_start.row(InlineKeyboardButton(text="Правила",
                                             callback_data="instructions"
                                             )
                        )
    keyboards_start.row(InlineKeyboardButton(text="Покупка",
                                             callback_data="buy"
                                             )
                        )
    keyboards_start.row(InlineKeyboardButton(text="Мой магазин",
                                             callback_data="my_shop",
                                             )
                        )
    keyboards_start.row(InlineKeyboardButton(text="Помощь",
                                             callback_data="help",
                                             )
                        )
    # брать ссылку на фото из бд
    try:
        await message.answer_photo(photo="AgACAgIAAxkBAAITtmQT0_aNtfTLlluxLZgMOyBZognTAALXwzEb_W2gSIK-252iJM_lAQADAgADcwADLwQ")
        await message.answer(text="Главное меню",
                             reply_markup=keyboards_start.as_markup())
    except AttributeError:
        await message.message.edit_text(text="Главное меню", reply_markup=keyboards_start.as_markup())