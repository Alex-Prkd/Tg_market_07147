from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ButtonBackInformationCostumer:
    def __init__(self):
        self.button_back = InlineKeyboardBuilder()
        self.button_back.row(InlineKeyboardButton(text="Назад",
                                                  callback_data="back_info_cost"))


class ButtonBackInformationSeller:
    def __init__(self):
        self.button_back = InlineKeyboardBuilder()
        self.button_back.row(InlineKeyboardButton(text="Назад",
                                                  callback_data="back_info_seller"))