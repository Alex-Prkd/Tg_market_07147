from aiogram.fsm.state import StatesGroup, State


class EditInfoFSM(StatesGroup):
    photo_bot = State()
    about_seller = State()
    instruction_seller = State()
    regulations_seller = State()
    about_costumer = State()
    instruction_costumer = State()
    regulations_costumer = State()


class AddSeller(StatesGroup):
    username_seller = State()


class AddUserToBlacklist(StatesGroup):
    username = State()


class DeleteUserToBlacklist(StatesGroup):
    username = State()


class SuperAdmin(StatesGroup):
    username = State()