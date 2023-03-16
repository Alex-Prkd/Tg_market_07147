from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup

__all__ = ["InformationSeller", "SettingMarket", "RegisterNameMarket"]


class InformationSeller:
    def __init__(self):
        self.keyboards = InlineKeyboardMarkup()
        about = InlineKeyboardButton(text="Почему мы?",
                                     callback_data='about_seller'
                                     )
        instruction = InlineKeyboardButton(text='Инструкция',
                                           callback_data="instruction_seller"
                                           )
        regulations_or_warning = InlineKeyboardButton(text="Правила",
                                                          callback_data="regulations_seller"
                                                      )
        acquainted = InlineKeyboardButton(text="Ознакомлен",
                                              callback_data="contact_with_admin"
                                          )
        self.keyboards.add(about)
        self.keyboards.add(instruction)
        self.keyboards.add(regulations_or_warning)
        self.keyboards.add(acquainted)


class SettingMarket:
    def __init__(self):
        # test_list = ["🌄 Фото", "🔠 Название", "ℹ Описание",
        #              "⚠ Товар", "🌎 Местоположение", "⬅ Назад",
        #              "➕ Добавить админа", "➖ Удалить админа"]
        list_settings = [
            [KeyboardButton(text="🌄 Фото")],
            [KeyboardButton(text="🔠 Название")],
            [KeyboardButton(text="ℹ Описание")],
            [KeyboardButton(text="⚠ Товар")],
            [KeyboardButton(text="🌎 Местоположение")],
            [KeyboardButton(text="⬅ Назад")],
            [KeyboardButton(text="➕ Добавить админа")],
            [KeyboardButton(text="➖ Удалить админа")]
        ]
        # list_settings = []
        # for i in test_list:
        #     list_settings.append(KeyboardButton(text=i))
        self.settings = ReplyKeyboardMarkup(list_settings,
                                            resize_keyboard=True,
                                            one_time_keyboard=True)


class RegisterNameMarket(StatesGroup):
    title = State()


    @staticmethod
    def confirmation_name():
        confirmation = InlineKeyboardMarkup()
        accept = InlineKeyboardButton(text="Да", callback_data="accept_name")
        cancel = InlineKeyboardButton(text="Нет", callback_data="acquainted_seller")

        confirmation.add(accept)
        confirmation.add(cancel)
        return confirmation
