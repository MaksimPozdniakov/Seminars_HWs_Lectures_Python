from random import choice as ch
from random import randint as ri

first_player = input('Введите свое имя: ')

bot_p = 'Бот Максим'
round = 1
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


def draw_board():
    global board
    for i in range(3):
        print(f' {board[i * 3]}   {board[i * 3 + 1]}   {board[i * 3 + 2]} ')

def lottery():
    print('Первый будет ходит Х, второй 0')
    print()
    print("Кто ходит первым: Введите 0 - если выбираете ОРЁЛ, 1 - если РЕШКА")
    mychoice = int(input())
    chance = ch([0, 1])
    print("Выпала РЕШКА") if chance else print("Выпал ОРЁЛ")
    if mychoice == chance:
        print("Вы ходите первым!")
        return 1
    else:
        print("Вы ходите вторым!")
        return 2
result = lottery()

def player():
    while True:
        step = int(input('Введите цифру от 1 до 9: '))
        if step > 9:
            print('Такой позиции нет. Введите цифру от 1 до 9!')
            continue
        else:
            break
    return step

def bot():
    step = ri(1, 9)
    return step

def steps_X(x, s):
    if s == 1:
        x[0] = 'X'
    if s == 2:
        x[1] = 'X'
    if s == 3:
        x[2] = 'X'
    if s == 4:
        x[3] = 'X'
    if s == 5:
        x[4] = 'X'
    if s == 6:
        x[5] = 'X'
    if s == 7:
        x[6] = 'X'
    if s == 8:
        x[7] = 'X'
    if s == 9:
        x[8] = 'X'
    return x

def steps_O(x, s):
    # step = int(input('Введите цифру от 1 до 9: '))
    if s == 1:
        x[0] = '0'
    if s == 2:
        x[1] = '0'
    if s == 3:
        x[2] = '0'
    if s == 4:
        x[3] = '0'
    if s == 5:
        x[4] = '0'
    if s == 6:
        x[5] = '0'
    if s == 7:
        x[6] = '0'
    if s == 8:
        x[7] = '0'
    if s == 9:
        x[8] = '0'
    return x

def chec_pozition_X():
    global board
    while True:
        if result == 1:
            player_step = player()
            if player_step not in board:
                print('Данная позиция уже занята!')
                continue
            else:
                board = steps_X(board, player_step)
                break
        else:
            player_step = bot()
            if player_step not in board:
                print('Данная позиция уже занята!')
                continue
            else:
                board = steps_X(board, player_step)
                break
    return board

def chec_pozition_0():
    global board
    while True:
        if result == 1:
            player_step = player()
            if player_step not in board:
                print('Данная позиция уже занята!')
                continue
            else:
                board = steps_O(board, player_step)
                break
        else:
            player_step = bot()
            if player_step not in board:
                print('Данная позиция уже занята!')
                continue
            else:
                board = steps_O(board, player_step)
                break
    return board

def win_conbination(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5]\
            or board[6] == board[7] == board[8] or board[0] == board[3] == board[6]\
            or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]\
            or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]: return 1
    else: return 2

while True:
    win = win_conbination(board)
    if win == 1:
        print('Игра окончена!')
        break

    if result == 1:
        print(f'Игрок {first_player} играет Х')
        print(f'Игрок {bot_p} играет 0')
        print()
        while True:
            if round == 1:
                print(f'{first_player} сделайте свой ход!')
                chec_pozition_X()
                round = 0
                result = 0
            else:
                print(f'{bot_p} сделайте свой ход!')
                chec_pozition_0()
                round = 1
                result = 1

            draw_board()
            win = win_conbination(board)
            if win == 1:
                break

    else:
        print(f'Игрок {bot_p} играет Х')
        print(f'Игрок {first_player} играет 0')
        print()
        while True:
            if round == 1:
                print(f'{bot_p} сделайте свой ход!')
                chec_pozition_X()
                round = 0
                result = 1
            else:
                print(f'{first_player} сделайте свой ход!')
                chec_pozition_0()
                round = 1
                result = 0

            draw_board()
            win = win_conbination(board)
            if win == 1:
                break


