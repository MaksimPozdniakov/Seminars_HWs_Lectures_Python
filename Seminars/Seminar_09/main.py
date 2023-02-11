from aiogram import executor
from handlers import dp

total = 150

async def on_start(_):  # запускаем ассинхронную функцию.
    print('Бот запущен')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)






