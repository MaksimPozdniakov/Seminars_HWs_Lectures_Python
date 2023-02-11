# # для начала создадим отдельный модуль, назовем его keyboards
# # импортируем библиотеку
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# # создаем переменную для нашей клавиатуры
# kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # чтобы после выбора клавиатура
#                                                                                  # сворачивалась, после True нужно
#                                                                                  # прописать one_time_keyboard=True
#
# # теперь создаем переменную для кнопок
# btn_pvp = KeyboardButton('/pvp')
# btn_help = KeyboardButton('/help')
# btn_location = KeyboardButton('/loc', request_location=True)   # request_location=True данная запись позволяет опр лок
# btn_contact = KeyboardButton('/num', request_contact=True)  # request_contact=True позволяет поделиться наш контактом
#
# # теперь мы перекидываем эти кнопки на клавиатуру
# kb_main_menu.add(btn_pvp, btn_help) # так кнопки будут в строчку
#
# kb_main_menu.add(btn_pvp)  # так в столбик
# kb_main_menu.add(btn_help)
#
# kb_main_menu.add(btn_location) # так мы вызываем 'Геолокация' с клавиатуры, после получения данных по локации можно
#                                # делать какие-то функции
# kb_main_menu.add(btn_contact) # так мы его вызываем
#
#
#
#
# # далее переходим в модуль handler
# # импортирем сюда наш модуль keyboards
# from keyboards import kb_main_menu
#
# @dp.message_handler(command=['start'])
# async def mes_start(message: types.Message):
#     await message.answer('Приветствую тебя! Ты на конфетном поле боя', reply_markup=kb_main_menu)
#
# @dp.message_handler(command=['help'])
# async def mes_start(message: types.Message):
#     await message.answer('Бог поможет', reply_markup=kb_main_menu)
#
# @dp.message_handler(content_types='location')
# async def mes_start(message: types.Message):
#     print(message)
#
# # добавляем таймер
# # нужна библиотека import asyncio import sleep
# import asyncio import sleep
#
# далее в каком-нибудь handlere, где там эта функция нужна мы прописываем
# await message.answer('3...')
# await sleep(3) # 3 это количество секкунд до переключения на след строку
# await message.answer('2...')
# await sleep(3)
# await message.answer('1...')
# await sleep(3)
# await message.answer('Fight...')



# для красоты используем библиотеку datetime
# from datetime import datetime
#
# users = []
# users.append(str(datetime.now()))  # в данном случае необходимо все перевести в строку
# users.append(str(message.from_user.full_name))
# users.append(str(message.from_user.id))
# users.append(str(message.from_user.username))
#
# тоже самое только через map
# users = list(map(str, users))
#
# with open('text.txt', 'a', encoding='UTF-8') as data:
# 	data.write(':'.join(users)+'\n') # join используем для красивого вывода информации




