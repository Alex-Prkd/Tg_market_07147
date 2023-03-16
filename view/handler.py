import os

from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db import Session
from db.commands.costumer import add_user
from keyboards import *

print(os.getenv("TOKEN"))
bot = Bot(token=os.getenv("TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())




seller_list = {}

"""Добавить в бд профиль"""


# Стартовое покупатель/продавец
@dp.message_handler(CommandStart())
async def command_start_menu(message: Message):
    async with Session() as session:
        await add_user(session, message.from_user)
    photo = open("image/haze_title.jpg", "rb")
    started_key = KeyboardStart()
    await message.answer_photo(photo,
                               reply_markup=started_key.keyboards
                               )


# __________________________________________Покупатель____________________________________________________________
@dp.callback_query_handler(lambda callback: callback.data in "instructions")
async def get_instruction(callback_query: CallbackQuery):
    information = InformationCostumer()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text="Ознакомьтесь",
                           reply_markup=information.keyboards
                           )



@dp.callback_query_handler(lambda callback: callback.data in ["about_costumer", "instruction_costumer",
                                                              "regulations_costumer"])
async def costumer_menu(callback_query: CallbackQuery):
        # информация из бд
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text=f"Выбрали: {callback_query.data}"
                           )


@dp.callback_query_handler(lambda callback: callback.data in "region")
async def select_region(callback_query: CallbackQuery):
    regions = LocationSeller()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text="Сделайте выбор",
                           reply_markup=regions.location)


# Выбор местоположения продавца
@dp.callback_query_handler(lambda callback: callback.data in ["sovetskiy", "partizanskiy",
                                                              "moscovskiy", "pervomaiskiy",
                                                              "oktyabrskiy", "tsentralnyy",
                                                              "never_mind"])
async def choice_product(callback_query: CallbackQuery):
    # Меню со всеми продавцами
    if callback_query.data == "never_mind":
        print("never_mind")
        products_kb = ChoiceProduct()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               text="Продукция",
                               reply_markup=products_kb.products)
    else:
        # Выбор продавцов из бд по геолакации
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               text=callback_query.data
                               )


# Список магазинов
# Здесь ещё подкинуть пагинацию (БЛЯЯЯТЬ)
@dp.callback_query_handler(lambda callback: callback.data in "shops")
async def get_shops(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text=callback_query.data
                           )


# Список продуктов
@dp.callback_query_handler(lambda callback: callback.data in ["aqua", "details", "vape", "brand",
                                                              "limit_vape", "nicotine"])
async def products_result_request(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=f"Выбрали {callback_query.data}")


@dp.callback_query_handler(lambda callback: callback.data in "help")
async def get_help(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text=f"Связь с админом: @alex_prkd",
                           )


# _____________________________________________________Продавец___________________________________________________

@dp.callback_query_handler(lambda callback: callback.data in "register_market")
async def seller_info(callback_query: CallbackQuery):
    print()
    print(callback_query.data)
    information = InformationSeller()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text="Ознакомьтесь",
                           reply_markup=information.keyboards)


# Информация для продавца
@dp.callback_query_handler(lambda callback: callback.data in ["about_seller", "instruction_seller",
                                                              "regulations_seller", "contact_with_admin"
                                                              ])
async def seller_menu(callback_query: CallbackQuery):
    print()
    print(callback_query.data)
    # Ознакомлен
    if callback_query.data == "contact_with_admin":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               text=f"Связь с админом: @alex_prkd",
                               )
    else:
        # Поиск информации по бд
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               text=f"Выбрали: {callback_query.data}\n"
                                    f"Поиск в бд по запросу"
                               )


@dp.callback_query_handler(lambda callback: callback.data in "my_shop")
async def get_my_shop(callback_query: CallbackQuery):
    print()
    print(callback_query.data)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text="У вас нет магазина, прочитайте правила для регистрации.",
                           )


# Выбор настроек магазина
# Не забудь прокинуть клавиаутуру для этого хендрера!!! ПОЖАЛУЙСТА!
@dp.message_handler(lambda msg: msg.text in ["🌄 Фото", "🔠 Название", "ℹ Описание",
                                             "⚠ Товар", "🌎 Местоположение", "⬅ Назад",
                                             "➕ Добавить админа", "➖ Удалить админа"])
async def settings_market(message: Message):
    print()
    print(message)
    if message.text == "⬅ Назад":
        await command_start_menu(message)
    else:
        if message.text == "🌄 Фото":
            await message.answer("Изменишь фото")
        elif message.text == "🔠 Название":
            await message.answer(text="Поменяешь название")
        elif message.text == "ℹ Описание":
            await message.answer(text="Добавишь описание")
        elif message.text == "⚠ Товар":
            await message.answer(text="Обновить товар")
        elif message.text == "🌎 Местоположение":
            await message.answer(text="Добавить местоположение")
        elif message.text == "➕ Добавить админа":
            await message.answer(message.text)
        elif message.text == "➖ Удалить админа":
            await message.answer(message.text)

        # Дописать хэндлеры на каждое изменение магазина


# __________________________________Админ__________________________________________________________
@dp.message_handler(commands="admin")
async def entry(message: Message):
    print()
    print(message)
    if message.from_user.id == ADMIN_ID:
        await message.answer(text="Введите пароль")
        await PasswordAdmin.password.set()
    else:
        await message.answer(text="Нет прав")


@dp.message_handler(state=PasswordAdmin.password)
async def validate_password(message: Message, state=FSMContext) -> None:
    await bot.delete_message(message.from_user.id, message.message_id)
    await state.update_data(password=message.text)
    password_user = await state.get_data()
    if password_user.get("password") == PASSWORD_ADMIN:
        await message.answer(text="Вошли",
                             reply_markup=AdminMenu.menu)
    else:
        await message.answer("Неверный пароль")
    await state.finish()


# Поменять == ADMIN_ID на !=ADMIN_ID?
@dp.message_handler(lambda msg: msg.text in ["Список магазинов", "Список покупателей", "Изменить информацию",
                                              "ЧС", "Выйти", "Назад", "Добавить локацию", "Удалить локацию"])
async def output_menu_admin(message: Message):
    if message.from_user.id == ADMIN_ID:
        if message.text == "Список магазинов":
            await message.answer(text="Из бд вынимаем список всех магазинов")
        elif message.text == "Список покупателей":
            await message.answer(text="Из бд вынимаем список всех покупателей")
        elif message.text == "Изменить информацию":
            role_selection = SelectRole
            await message.answer("Выберите пункт",
                                 reply_markup=role_selection.costumer_or_seller
                                 )
        elif message.text == "Добавить локацию":
            await message.answer("Добавить локацию")
        elif message.text == "Удалить локацаию":
            await message.answer("Решить вопрос с каскдным удалением")
        elif message.text == "Выйти":
            await command_start_menu(message)
        elif message.text == "Назад":
            await message.answer(text="Вошли", reply_markup=AdminMenu.menu)
    else:
        await message.answer(text="Нет доступа")


@dp.message_handler(lambda msg: msg.text in ["О продавце", "О покупателе", "Назад"])
async def edit_info(message: Message):
    if message.from_user.id == ADMIN_ID:
        if message.text == "Назад":
            await output_menu_admin(message)
        else:
            new_info = EditInfo(message.text)
            await message.answer(text="список инфы о боте", reply_markup=new_info.keyboards)



# не работает кнопка "почему мы"?? callback.data is "edit_about_costumer"
@dp.callback_query_handler(lambda callback: callback.data in ["edit_regulations_seller", "edit_instruction_seller",
                                                              "edit_regulations_costumer", "edit_instruction_costumer",
                                                              "edit_about_costumer", "about_seller", "about_costumer"])
async def edit_info_seller(callback: CallbackQuery):
    if callback.from_user.id == ADMIN_ID:
        await bot.answer_callback_query(callback.id)
        await bot.send_message(chat_id=callback.from_user.id, text=callback.data)
