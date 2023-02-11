import model
import view

def input_handler(inp: int):
    match inp:
        case 1:
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 2:
            view.show_all(model.db_list)
        case 3:
            view.show_result(model.db_list)
        case 4:
            view.change_contact(model.db_list)
        case 5:
            view.create_contact(model.db_list)
        case 6:
            view.del_contact(model.db_list)
        case 7:
            model.change_file('database.txt', model.db_list)
        case 8:
            view.exit_program()

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)



