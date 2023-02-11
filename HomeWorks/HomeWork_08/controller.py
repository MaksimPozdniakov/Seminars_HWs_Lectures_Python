import view
import model

def input_handler(inp: int):
    match inp:
        case 1:
            our_class = model.choice_class()
            model.open_file(our_class)
            view.state_journal(model.main_dict)
        case 2:
            view.all_students(model.main_dict)
        case 3:
            view.magic(model.main_dict)
        case 4:
            our_class = model.choice_class()
            model.save_changes(our_class, model.main_dict)
            pass
        case 5:
            subject = view.add_student(model.main_dict)
            model.add_student2(model.main_dict, subject)
        case 6:
            view.add_subject(model.main_dict)
        case 7:
            model.clouse_journal()


def start():
    while True:
        user_inp = view.journal_menu()
        input_handler(user_inp)


