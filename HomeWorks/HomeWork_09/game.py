from random import choice as ch
from random import randint as ri
import botAndplayer
from aiogram import types


user_data = {}
min_candy = 100
max_candy = 200
user_log = ''

def create_users_log(time, user_name, full_name, user_id):
    global user_log
    user_log = str(time) + ' ' + 'Nik:' + ' ' + str(user_name) + ' ' + 'Имя:' + ' ' + str(full_name) + ' ' + 'ID:' + \
               ' ' + str(user_id) + '\n'
    return user_log

def random_candy(min_candy, max_candy):
    total_candies = ri(min_candy, max_candy)
    return total_candies

total = random_candy(min_candy, max_candy)

def update_dict(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {'candy_total': total, 'change_total': total,
                               'level': botAndplayer.level}

def show_candy(user):
    text = 'change_total'
    for key, value in user_data.items():
        if key == user:
            for i, j in user_data[key].items():
                if i == text:
                    return user_data[key][i]

def candies(user, take: int):
    text = 'change_total'
    for key, value in user_data.items():
        if key == user:
            for i, j in user_data[key].items():
                if i == text:
                    user_data[key][i] -= take
    return user_data

def lottery():
    chance = ch([0, 1])
    if chance:
        return True
    else:
        return False

def check_total(user):

    if show_candy(user) == 0:
        return True
    else:
        return False





