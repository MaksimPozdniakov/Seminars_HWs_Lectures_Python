import game
from random import randint as ri

level = 'hard'

def bot_step(user):
    total = game.show_candy(user)
    if level == 'hard':
        if total <= 28:
            take = total
        else:
            take = total % 29 if total % 29 != 0 else ri(1, 29)
        return take
    else:
        if total <= 28:
            take = total
        else:
            take = ri(1, 28)
        return take



def player_step(user, take: str):
    total = game.show_candy(user)
    if take.isdigit():
        take = int(take)
        if take <= 0 or take > 28:
            return False
        elif take > total:
            return False
        else:
            return True
    else:
        return False





