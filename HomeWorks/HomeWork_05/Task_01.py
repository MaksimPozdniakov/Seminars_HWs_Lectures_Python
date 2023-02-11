# Задача №1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход.

from random import randint as ri
from random import choice as ch

task = '''Условие задачи: На столе лежит заданное количество конфет. Вы пытаетесь обыкрать компьютер делая ход друг 
после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты 
оппонента достаются сделавшему последний ход.'''


all_sweets = 150

player = input('Как вас зовут? ')
bot = 'Бот Максим'

def lottery():
    print(task)
    print()
    print("Кидаем монетку: введите 0 - если выбираете ОРЁЛ, 1 - если РЕШКА")
    mychoice = int(input())
    chance = ch([0, 1])
    print("Выпала РЕШКА") if chance else print("Выпал ОРЁЛ")
    if mychoice == chance:
        print("Вы ходите первым!")
        return 1
    else:
        print("Первым ходит бот Максим!")
        return 2
result = lottery()

def bot1(x):
    if x <= 28:
        sweets = x

    else:
        sweets = x % 29 if x % 29 != 0 else ri(1, 29)

    return sweets

def player1(x):
    while True:
        print()
        sweets = int(input('Сколько конфет берете? '))
        if sweets > 28 or sweets < 1:
            print()
            print('Нельзя брать меньше 1 и больше 28 конфет!')
            continue

        if sweets > all_sweets:
            print()
            print('Столько конфет на столе нет!')
            continue
        else:
            break
    return sweets

while all_sweets > 0:

    if result == 1:
        while True:
            sweets = player1(all_sweets)
            print()
            print(f'Игрок {player} взял {sweets}')
            result = 0

            all_sweets = all_sweets - sweets
            print(f'На столе осталось {all_sweets}')

            if all_sweets == 0:
                print()
                print(f'Ура! Победил игрок {player}')
            break

    else:
        while True:
            sweets = bot1(all_sweets)
            print()
            print(f'{bot} взял {sweets}')
            result = 1

            all_sweets = all_sweets - sweets
            print(f'На столе осталось {all_sweets}')

            if all_sweets == 0:
                print()
                print(f'Извини друг, но победил {bot}')
            break


























