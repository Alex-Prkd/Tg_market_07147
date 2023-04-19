from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

ADMIN_ID = 610280722


__all__ = ["ADMIN_ID", "AdminMenu", "SelectRole", "EditInfo",
           "KeyboardBlacklist"]


class AdminMenu:
    def __init__(self):
        self.admin_menu = InlineKeyboardBuilder()
        self.admin_menu.row(InlineKeyboardButton(text="Добавить продавца",
                                                 callback_data="add_seller"))
        self.admin_menu.row(InlineKeyboardButton(text="Список магазинов",
                                                 callback_data="get_shops"))
        self.admin_menu.row(InlineKeyboardButton(text="Список пользователей",
                                                 callback_data="get_costumers"))
        self.admin_menu.row(InlineKeyboardButton(text="Изменить иформацию",
                                                 callback_data="edit_info_bot"))
        self.admin_menu.row(InlineKeyboardButton(text="ЧС",
                                                 callback_data="blacklist"))
        self.admin_menu.row(InlineKeyboardButton(text="Изменить фотографию главного меню",
                                                 callback_data="edit_photo_main_menu"))
        self.admin_menu.row(InlineKeyboardButton(text="Добавить админа",
                                                 callback_data="add_admin_bot"))
        self.admin_menu.row(InlineKeyboardButton(text="Выйти",
                                                 callback_data="home"))


class SelectRole:
    def __init__(self):
        self.role = InlineKeyboardBuilder()
        self.role.row(InlineKeyboardButton(text="Поменять информацию продавца",
                                           callback_data="edit_info_seller"))
        self.role.row(InlineKeyboardButton(text="Поменять информацию покупателя",
                                           callback_data="edit_info_costumer"))
        self.role.row(InlineKeyboardButton(text="Назад",
                                           callback_data="back_to_admin_menu"))


class EditInfo:
    def __init__(self, role):
        self.edit = InlineKeyboardBuilder()
        if role == "edit_info_costumer":
            self.edit.row(InlineKeyboardButton(text="Почему мы?",
                                               callback_data="edit_about_costumer"))
            self.edit.row(InlineKeyboardButton(text='Инструкция',
                                               callback_data="edit_instruction_costumer"))
            self.edit.row(InlineKeyboardButton(text="Правила",
                                               callback_data="edit_regulations_costumer"))
        elif role == "edit_info_seller":
            self.edit.add(InlineKeyboardButton(text="Почему мы?",
                                               callback_data="edit_about_seller"))
            self.edit.add(InlineKeyboardButton(text='Инструкция',
                                               callback_data="edit_instruction_seller"))

            self.edit.add(InlineKeyboardButton(text="Правила",
                                               callback_data="edit_regulations_seller"))
        self.edit.row(InlineKeyboardButton(text="Назад",
                                           callback_data="back_to_admin_menu"))


# MenuBlacklist
class KeyboardBlacklist:
    def __init__(self):
        self.blacklist_k = InlineKeyboardBuilder()
        self.blacklist_k.row(InlineKeyboardButton(text="Список пользователей",
                                                  callback_data="all_blacklist"))
        self.blacklist_k.row(InlineKeyboardButton(text="Добавить в ЧС",
                                                  callback_data="add_to_blacklist"))
        self.blacklist_k.row(InlineKeyboardButton(text="Удали из ЧС",
                                                  callback_data="delete_in_blacklist"))
        self.blacklist_k.row(InlineKeyboardButton(text="Назад",
                                                  callback_data="back_to_admin_menu"))
