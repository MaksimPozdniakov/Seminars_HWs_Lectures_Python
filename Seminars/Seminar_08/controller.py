import model
import view


def input_handler(inp: int):
    match inp:
        case 1:
            model.read_db('7A.txt')

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)






