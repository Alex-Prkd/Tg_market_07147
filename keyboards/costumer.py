from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

location = {"sovetskiy": "Советский", "partizanskiy": "Партизанский",
            "pervomaiskiy": "Первомайский", "oktyabrskiy": "Октябрьский",
            "moskovskiy": "Московский", "tsentralnyy": "Центральный",
            "never_mind": "Неважно", "home": "Назад"}

products = {"aqua": "Жидкость", "brand": "Марка жидкости",
            "details": "Расходники", "vape": "Вейпы",
            "limit_vape": "Одноразки", "nicotine": "Снюс",
            "all_shops": "Все магазины", "back": "Назад"}

__all__ = ["location", "products", "InstructionCostumer",
           "ChoiceProduct", "LocationSeller"
           ]


class InstructionCostumer:
    def __init__(self):
        self.keyboards_info = InlineKeyboardBuilder()
        self.keyboards_info.row(InlineKeyboardButton(text="Почему мы?",
                                                     callback_data="about_costumer")
                                )
        self.keyboards_info.row(InlineKeyboardButton(text='Инструкция',
                                                     callback_data="instruction_costumer"
                                                     )
                                )
        self.keyboards_info.row(InlineKeyboardButton(text="Правила участников",
                                                     callback_data="regulations_costumer"
                                                     )
                                )
        self.keyboards_info.row(InlineKeyboardButton(text="Регистрация магазина",
                                                     callback_data="register_market"
                                                     )
                                )
        self.keyboards_info.row(InlineKeyboardButton(text="Главное меню",
                                                     callback_data="home"))


# принимаются данные с вьюхи choice_costumer просиходит поиск по бд
class LocationSeller:
    def __init__(self):
        self.location = InlineKeyboardBuilder()
        for en_local, ru_local in location.items():
            self.location.row(InlineKeyboardButton(text=ru_local,
                                                   callback_data=en_local)
                              )


# в передача в класс словаря с данныит из бд
class ChoiceProduct:
    def __init__(self):
        self.products = InlineKeyboardBuilder()
        for en_product, ru_product in products.items():
            self.products.row(InlineKeyboardButton(text=ru_product,
                                                   callback_data=en_product)
                              )