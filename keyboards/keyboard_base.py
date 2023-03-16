from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

__all__ = ["KeyboardStart"]


class KeyboardStart:
    def __init__(self):
        self.keyboards = InlineKeyboardMarkup()
        shops = InlineKeyboardButton(text="Список магазинов",
                                     callback_data="shops"
                                     )
        instructions = InlineKeyboardButton(text="Правила",
                                            callback_data="instructions"
                                            )
        region = InlineKeyboardButton(text="Выбрать район",
                                      callback_data="region"
                                      )
        help_admin = InlineKeyboardButton(text="Помощь",
                                          callback_data="help"
                                          )
        my_shop = InlineKeyboardButton(text="Мой магазин",
                                       callback_data="my_shop")
        self.keyboards.add(shops)
        self.keyboards.add(instructions)
        self.keyboards.add(region)
        self.keyboards.add(help_admin)
        self.keyboards.add(my_shop)

    # Отдельный файл клавитатуры
    @staticmethod
    def cancel():
        kb = [
            [KeyboardButton(text="⛔ Отмена")]
        ]
        cancel = ReplyKeyboardMarkup(kb, resize_keyboard=True,
                                     one_time_keyboard=True
                                     )
        return cancel
