from aiogram import Bot
from aiogram.types import CallbackQuery

from keyboards import ButtonBackInformationCostumer
from keyboards.costumer import InstructionCostumer, LocationSeller, ChoiceProduct


# поменять название
async def instruction(callback_query: CallbackQuery):
    information_buttons = InstructionCostumer().keyboards_info
    await callback_query.message.edit_text(text="Ознакомьтесь",
                                           reply_markup=information_buttons.as_markup())


async def about_costumer(callback_query: CallbackQuery):
        # информация из бд
    btn_home = ButtonBackInformationCostumer().button_back
    await callback_query.message.edit_text(text=f"Сюда приходит инфа из бд '{callback_query.data}'",
                                           reply_markup=btn_home.as_markup())


async def get_help(callback_query: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text=f"Связь с админом: @alex_prkd",
                           )


async def select_region(callback_query: CallbackQuery):
    regions = LocationSeller().location
    await callback_query.message.edit_text(text="Сделайте выбор",
                                           reply_markup=regions.as_markup())


async def choice_product(callback_query: CallbackQuery):
    # Меню со всеми продавцами
    if callback_query.data == "never_mind":
        products_kb = ChoiceProduct().products
        await callback_query.message.edit_text(text="Продукция",
                                               reply_markup=products_kb.as_markup())
    else:
        # Выбор продавцов из бд по геолакации
        await callback_query.message.edit_text(text=callback_query.data)


async def get_products(callback_query: CallbackQuery):
    # Список продуктов
    await callback_query.message.edit_text(text="Выбрали")


async def all_shops(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Добавить инлайн-клаву для всех магазов из"
                                           "бд + не забыть добавить кнопку 'назад'")
