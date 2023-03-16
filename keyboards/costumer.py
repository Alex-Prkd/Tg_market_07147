from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

location = {"sovetskiy": "Советский", "partizanskiy": "Партизанский",
            "pervomaiskiy": "Первомайский", "oktyabrskiy": "Октябрьский",
            "moskovskiy": "Московский", "tsentralnyy": "Центральный",
            "never_mind": "Неважно"}


products = {"aqua": "Жидкость", "brand": "Марка жидкости",
            "details": "Расходники", "vape": "Вейпы",
            "limit_vape": "Одноразки", "nicotine": "Снюс"}


__all__ = ["location", "products", "InformationCostumer",
           "ChoiceProduct", "LocationSeller"
           ]


class InformationCostumer:
    def __init__(self):
        self.keyboards = InlineKeyboardMarkup()
        about = InlineKeyboardButton(text="Почему мы?",
                                     callback_data='about_costumer'
                                     )
        instruction = InlineKeyboardButton(text='Инструкция',
                                           callback_data="instruction_costumer"
                                           )
        regulations_or_warning = InlineKeyboardButton(text="Правила участников",
                                                      callback_data="regulations_costumer"
                                                      )
        register_market = InlineKeyboardButton(text="Регистрация магазина",
                                               callback_data="register_market"
                                               )
        self.keyboards.add(about)
        self.keyboards.add(instruction)
        self.keyboards.add(regulations_or_warning)
        self.keyboards.add(register_market)


# принимаются данные с вьюхи choice_costumer просиходит поиск по бд
class LocationSeller:
    def __init__(self):
        self.location = InlineKeyboardMarkup()
        for en_local, ru_local in location.items():
            self.location.add(InlineKeyboardButton(text=ru_local,
                                                   callback_data=en_local)
                              )


# в передача в класс словаря?
class ChoiceProduct:
    def __init__(self):
        self.products = InlineKeyboardMarkup()
        for en_product, ru_product in products.items():
            self.products.add(InlineKeyboardButton(text=ru_product,
                                                   callback_data=en_product)
                              )