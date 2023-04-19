from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MainMenu:
    def __init__(self):
        self.keyboards_start = InlineKeyboardBuilder()
        self.keyboards_start.row(InlineKeyboardButton(text="Правила",
                                                      callback_data="instructions")
                                 )
        self.keyboards_start.row(InlineKeyboardButton(text="Покупка",
                                                      callback_data="buy")
                                 )
        self.keyboards_start.row(InlineKeyboardButton(text="Мой магазин",
                                                      callback_data="my_shop",)
                                 )
        self.keyboards_start.row(InlineKeyboardButton(text="Помощь",
                                                      callback_data="help",)
                                 )


class ButtonBackInformationCostumer:
    def __init__(self):
        self.button_back = InlineKeyboardBuilder()
        self.button_back.row(InlineKeyboardButton(text="Назад",
                                                  callback_data="back_info_cost")
                             )


class ButtonBackInformationSeller:
    def __init__(self):
        self.button_back = InlineKeyboardBuilder()
        self.button_back.row(InlineKeyboardButton(text="Назад",
                                                  callback_data="back_info_seller")
                             )
