import game
from aiogram import types

def get_candy_ending(user):
    candy = game.show_candy(user)
    # candy = abs(count)
    candy %= 100
    if 5 <= candy <= 20:
        return 'конфет'
    candy %= 10
    if candy == 1:
        return 'конфета'
    elif 2 <= candy <= 4:
        return 'конфеты'
    else:
        return 'конфет'

def get_candy_for_bot(count: int):
    candy = abs(count)
    candy %= 100
    if 5 <= candy <= 20:
        return 'конфет'
    candy %= 10
    if candy == 1:
        return 'конфету'
    elif 2 <= candy <= 4:
        return 'конфеты'
    else:
        return 'конфет'

def get_candy_start(count: int):
    candy = abs(count)
    candy %= 100
    if 5 <= candy <= 20:
        return 'конфет'
    candy %= 10
    if candy == 1:
        return 'конфета'
    elif 2 <= candy <= 4:
        return 'конфеты'
    else:
        return 'конфет'


rules_game = f'Правила максимально просты. \n' \
             f'На столе лежит {game.total} {get_candy_start(game.total)}. ' \
             f'Тебе нужно обыграть компьютер делая ход друг после друга. Первый ход определяется жеребьёвкой. ' \
             f'За один ход можно забрать не более чем 28 конфет. Все конфеты достаются сделавшему последний ход.'


def write_log(data: str):
    with open('user_logs.txt', 'a', encoding='UTF-8') as user_log:
        user_log.write(data)

