from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


ADMIN_ID = 610280722
PASSWORD_ADMIN = "padmin"


__all__ = ["ADMIN_ID", "PASSWORD_ADMIN", "PasswordAdmin",
           "AdminMenu", "EditInfo", "SelectRole"]


class PasswordAdmin(StatesGroup):
    password = State()


class AdminMenu:
    kb = [
        [KeyboardButton(text="Список магазинов")],
        [KeyboardButton(text="Список покупателей")],
        [KeyboardButton(text="Добавить локацию")],
        [KeyboardButton(text="Удалить локацию")],
        [KeyboardButton(text="Изменить информацию")],
        [KeyboardButton(text="ЧС")],
        [KeyboardButton(text="Выйти")]
    ]

    menu = ReplyKeyboardMarkup(keyboard=kb,
                               resize_keyboard=True,
                               one_time_keyboard=True
                               )


class SelectRole:
    kb = [
        [KeyboardButton(text="О покупателе")],
        [KeyboardButton(text="О продавце")],
        [KeyboardButton(text="Назад")]
    ]
    costumer_or_seller = ReplyKeyboardMarkup(keyboard=kb,
                                             resize_keyboard=True,
                                             one_time_keyboard=True
                                             )


class EditInfo:
    def __init__(self, role):
        self.keyboards = InlineKeyboardMarkup()
        if role == "О покупателе":
            about = InlineKeyboardButton(text="Почему мы?",
                                         callback_data="edit_about_costumer"
                                         )
            instruction = InlineKeyboardButton(text='Инструкция',
                                               callback_data="edit_instruction_costumer"
                                               )
            regulations_or_warning = InlineKeyboardButton(text="Правила",
                                                          callback_data="edit_regulations_costumer"
                                                          )
        else:
            about = InlineKeyboardButton(text="Почему мы?",
                                         callback_data="edit_about_seller"
                                         )
            instruction = InlineKeyboardButton(text='Инструкция',
                                               callback_data="edit_instruction_seller"
                                               )
            regulations_or_warning = InlineKeyboardButton(text="Правила",
                                                          callback_data="edit_regulations_seller"
                                                          )

        self.keyboards.add(about)
        self.keyboards.add(instruction)
        self.keyboards.add(regulations_or_warning)
