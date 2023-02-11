from create import dp
from aiogram import types
import text_game
import game
import botAndplayer
from datetime import datetime
from keyboards import kb_main_menu

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! Давай поиграем в игру.\n'
                         f'{text_game.rules_game} '
                         f'Положись на удачу нажми на -> /lottery', reply_markup=kb_main_menu)

    user_id = message.from_user.id
    time = datetime.now().strftime('%d %B в %H:%M')
    user_name = message.from_user.username
    full_name = message.from_user.full_name

    game.create_users_log(time, user_name, full_name, user_id)
    text_game.write_log(game.user_log)

    game.user_data[user_id] = {'candy_total': game.total, 'change_total': game.total,
                               'level': botAndplayer.level}

@dp.message_handler(commands=['eazy'])
async def eazy_game(message: types.Message):
    botAndplayer.level = 'eazy'
    game.update_dict(message)
    await message.answer(f'{message.from_user.first_name}, ты отнял у меня мозги, но я сомневаюсь, что тебе это поможет'
                         f' На столе {game.total} {text_game.get_candy_start(game.total)}')
    await lottery_new(message)

@dp.message_handler(commands=['hard'])
async def hard_game(message: types.Message):
    botAndplayer.level = 'hard'
    game.update_dict(message)
    await message.answer(f'{message.from_user.first_name}, я смотру ты решил поиграть с огнем. Ну попробуй!'
                         f' На столе {game.total} {text_game.get_candy_start(game.total)}')
    await lottery_new(message)

@dp.message_handler(commands=['show_level'])
async def show_level(message: types.Message):
    await message.answer(f'Сейчас ты играешь на {botAndplayer.level}')

@dp.message_handler(commands=['new_game'])
async def game_new(message: types.Message):
    game.update_dict(message)

    await message.answer('Количество попыток не увеличивает твои шансы на победу!!!'
                         f' На столе {game.total} {text_game.get_candy_start(game.total)}')
    await lottery_new(message)

@dp.message_handler(commands=['lottery'])
async def lottery_new(message: types.Message):
    if game.lottery():
        await message.answer(f'Первым ходит {message.from_user.first_name}')
        await player(message)
    else:
        await message.answer('Первым ходит Бот')
        await game_bot(message)

async def player(message: types.Message):
    await message.answer(f'{message.from_user.first_name} твой ход')

@dp.message_handler()
async def game_player(message: types.Message):
    user_id = message.from_user.id
    if botAndplayer.player_step(user_id, message.text):
        take = int(message.text)
        sweets = game.candies(user_id, take)

        await message.answer(f'Прекрасно на столе осталось {game.show_candy(user_id)} '
                             f'{text_game.get_candy_ending(user_id)}')
        if game.check_total(user_id):
            await message.answer(f'Вот и все! Победил {message.from_user.first_name}'
                                 ' Попробуй повторить -> /new_game\n'
                                 'Если ты снова поверил в себя, то можешь вернуть мне мозги -> /hard')
        else:
            await game_bot(message)
    else:
        await message.answer('Ты смотри какой умный! Брать можно от 1 до 28 конфет и указывать это только цифрами,'
                             f' если что, на столе осталось {game.show_candy(user_id)}'
                             f' {text_game.get_candy_ending(user_id)}')
        await player(message)


async def game_bot(message):
    user_id = message.from_user.id
    take = botAndplayer.bot_step(user_id)
    sweets = game.candies(user_id, take)
    await message.answer(f'Бот взял {take} {text_game.get_candy_for_bot(take)}. На столе осталось'
                         f' {game.show_candy(user_id)} {text_game.get_candy_for_bot(user_id)}')
    if game.check_total(user_id):
        await message.answer('Чего и следовало доказать! Победил Бот! У тебя есть шанс отомстить этой железяке. Если'
                             ' ты готов, то нажми на -> /new_game\n'
                             'Если ты начинаешь терять веру в себя, то нажми на команду -> /eazy')
    else:
        await player(message)







