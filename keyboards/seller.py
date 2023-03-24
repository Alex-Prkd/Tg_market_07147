from aiogram.types import InlineKeyboardButton

__all__ = ["InformationSeller"]

from aiogram.utils.keyboard import InlineKeyboardBuilder


class InformationSeller:
    def __init__(self):
        self.keyboards = InlineKeyboardBuilder()
        self.keyboards.row(InlineKeyboardButton(text="Почему мы?",
                                                callback_data='about_seller'
                                                ))
        self.keyboards.row(InlineKeyboardButton(text='Инструкция',
                                                callback_data="instruction_seller"
                                                ))
        self.keyboards.row(InlineKeyboardButton(text="Правила",
                                                callback_data="regulations_seller"
                                                ))
        self.keyboards.row(InlineKeyboardButton(text="Ознакомлен",
                                                callback_data="contact_with_admin"
                                                ))
        self.keyboards.row(InlineKeyboardButton(text="Назад",
                                                callback_data="home"))


class SettingMarket:
    """ Эта клавиатура будет работать,
     когда подкину бд и создам магазин т.к. некуда реализовывать"""

    def __init__(self):
        self.settings_market = InlineKeyboardBuilder()
        self.settings_market.row(InlineKeyboardButton(text="Изменить фото",
                                                      callback_data="edit_photo"))
        self.settings_market.row(InlineKeyboardButton(text="Поменять название",
                                                      callback_data="edit_title"))
        self.settings_market.row(InlineKeyboardButton(text="Изменить описание",
                                                      callback_data="edit_description"))
        self.settings_market.row(InlineKeyboardButton(text="Обновить товар",
                                                      callback_data="edit_product"))
        self.settings_market.row(InlineKeyboardButton(text="Изменить местоположение",
                                                      callback_data="edit_location"))
        self.settings_market.row(InlineKeyboardButton(text="Добавить админа",
                                                      callback_data="add_admin"))
        self.settings_market.row(InlineKeyboardButton(text="Удалить админа",
                                                      callback_data="delete_admin"))
