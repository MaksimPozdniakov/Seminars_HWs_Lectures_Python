# что такое handlers - это функионал нашего dispatchera
from create import dp
from aiogram import types

@dp.message_handler(commands=['start'])
async def mes_start(massage: types.Message):              # massage - это целый объект, в который вшито очень много
                                                          # информации. Это и id чата, id юзера, время
                                                          # когда отправленно сообщение и так далее.
    await massage.answer(f'Привет, {massage.from_user.first_name}!')    # await - я обещаю выполнить свои обяз, когда
                                                                        # мне вернется необход информация

@dp.message_handler(commands=['help'])
async def mes_help(massage: types.Message):
    await massage.answer('Пока я еще ничего не умею, но обязательно научусь')

@dp.message_handler(commands=['set'])
async def mes_settings(massage: types.Message):
    global total
    count = int(massage.text.split()[1])
    total = count
    await massage.answer(f'Максимальное кол-во конфет установленно {total} ')

@dp.message_handler(text='Бла')
async def mes_all(massage: types.Message):
    await massage.answer('Бла бла бла')

@dp.message_handler()                                    # в handler аргументов нет, и теперь он подхватывает любую
                                                         # команду
async def mes_all(massage: types.Message):
    global total
    if massage.text.isdigit():
        total -= int(massage.text)
        await massage.answer(f'На столе осталось {total} конфет')


