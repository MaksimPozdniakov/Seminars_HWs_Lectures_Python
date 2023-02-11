from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_new_game = KeyboardButton('/new_game')
btn_show_level = KeyboardButton('/show_level')

kb_main_menu.add(btn_new_game, btn_show_level)

