__all__ = ["start_command", "admin", "costumer", "seller", "start_commands",
           "menu_costumer", "menu_seller", "menu_admin"]

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from view.start_command import command_start_menu

from view.admin import start_admin_menu, get_shops, get_costumers, select_role, blacklist, \
    edit_info

from view.costumer import instruction, about_costumer, get_help, select_region, choice_product, get_products, all_shops

from view.seller import get_my_shop, get_info_seller, edit_photo, edit_title, edit_description, edit_product, \
    edit_location, add_admin, delete_admin


def start_commands(router: Router):
    router.message.register(command_start_menu, CommandStart())
    router.message.register(start_admin_menu, Command("admin"))


def menu_costumer(router: Router):
    router.callback_query.register(instruction, lambda call: call.data in ["instructions", "back_info_cost"])
    router.callback_query.register(command_start_menu, F.data == "home")
    router.callback_query.register(about_costumer, lambda call: call.data in ["about_costumer", "instruction_costumer",
                                                                              "regulations_costumer",
                                                                              "register_market"])
    router.callback_query.register(get_help, F.data == "help")
    router.callback_query.register(select_region, lambda call: call.data in ["buy", "back"])
    router.callback_query.register(all_shops, F.data == "all_shops")
    # сделать функцию/файл при вызове возвращает список?
    router.callback_query.register(choice_product, lambda call: call.data in ["sovetskiy", "partizanskiy",
                                                                              "moscovskiy", "pervomaiskiy",
                                                                              "oktyabrskiy", "tsentralnyy",
                                                                              "never_mind"])
    router.callback_query.register(get_products, lambda call: call.data in ["aqua", "details", "vape", "brand",
                                                                            "limit_vape", "nicotine"])


def menu_seller(router: Router):
    router.callback_query.register(get_my_shop, lambda call: call.data in ["my_shop", "back_info_seller"])
    router.callback_query.register(get_info_seller, lambda call: call.data in ["about_seller", "instruction_seller",
                                                                               "regulations_seller",
                                                                               "contact_with_admin"])
    router.callback_query.register(edit_photo, F.data == "edit_photo")
    router.callback_query.register(edit_title, F.data == "edit_title")
    router.callback_query.register(edit_description, F.data == "edit_description")
    router.callback_query.register(edit_product, F.data == "edit_product")
    router.callback_query.register(edit_location, F.data == "edit_location")
    router.callback_query.register(add_admin, F.data == "add_admin")
    router.callback_query.register(delete_admin, F.data == "delete_admin")


def menu_admin(router: Router):
    router.callback_query.register(start_admin_menu, F.data == "back_to_admin_menu")
    router.callback_query.register(get_shops, F.data == "get_shops")
    router.callback_query.register(get_costumers, F.data == "get_costumers")
    router.callback_query.register(select_role, F.data == "edit_info_bot")
    router.callback_query.register(blacklist, F.data == "blacklist")
    router.callback_query.register(edit_info, lambda call: call.data in ["edit_info_costumer",
                                                                         "edit_info_seller"])

                                                # ["edit_regulations_seller", "edit_instruction_seller",
                                                #  "edit_regulations_costumer", "edit_instruction_costumer",
                                                #  "edit_about_costumer", "about_seller", "about_costumer"])
