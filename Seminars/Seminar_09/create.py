from aiogram import Bot, Dispatcher

bot = Bot('6023753959:AAHUXngZ17n0pIhtEN0gogAdGIkLy-8T_zs')    # наш бот. Что такое TOKEN - это цифровой ключь, который
                                                               # позволяет работать с нашим ботом


dp = Dispatcher(bot)                                           # модуль отвечающий за входящие сообщения от
                                                               # пользователя. В него мы передаем наш бот



