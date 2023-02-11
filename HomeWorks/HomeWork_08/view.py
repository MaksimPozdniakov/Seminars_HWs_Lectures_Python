def journal_menu():
    print('Главное меню')
    print('\tОткрыть журнал - 1\n'
          '\tПоказать общий список учеников - 2\n'
          '\tПоказать список учеников по конкретному предмету - 3\n'
          '\tСохранить изменения - 4\n'
          '\tДобавить нового ученика - 5\n'
          '\tДобавить новый предмет - 6\n'
          '\tЗакрыть журнал - 7\n')
    while True:
        user_choise = int(input('\tСделайте выбор: '))
        if user_choise < 1 or user_choise > 7:
            print('\tВ меню такого пункта нет.')
            continue
        else:
            break
    return user_choise

def state_journal(md: dict):
    if md:
        print('Журнал открыт')
        return True
    else:
        print('Журнал закрыт')
        return False

def search_subject(md: dict) -> dict:
    pup_id = 1
    result = None
    new_dict = dict()

    while True:
        user_choise = input('\tВыберите предмет: ')
        for key, value in md.items():
            if key == user_choise:
                for item_k, item_v in value.items():
                    new_dict[item_k] = item_v
                    marks = ' '
                    for i in item_v:
                        for j in i:
                            marks += j + ' '
                    print(f'{pup_id}: {item_k} - список оценок: {marks}')
                    pup_id += 1
                result = 1
                break
            else:
                result = 2
        if result == 2:
            print('В журнале такого предмета нет')
            continue
        else:
            break
    return new_dict

def who_answer():
    return input('Введите полностью имя и фамилию того, кто будет отвечать: ')

def what_mark():
    return input('На какую оценку ответил? ')

def magic(md: dict) -> dict:
    our_subjects = search_subject(md)
    our_student = who_answer()
    our_mark = what_mark()
    our_subjects[our_student].append(our_mark)
    return our_subjects

def add_student(md: dict):
    subject = search_subject(md)
    new_student = input('Введите через пробел фамилию и имя новуго ученика: ')
    new_marks = []
    subject[new_student] = new_marks
    return subject

def sup_add_sub() -> dict:
    my_dict = dict()
    new_student = input('Введите через пробел фамилию и имя новуго ученика: ')
    new_marks = []
    my_dict[new_student] = new_marks
    return my_dict

def add_subject(md: dict):
    new_subject = input('Введите название нового предмета: ')
    new_students = sup_add_sub()
    md[new_subject] = new_students
    return md

def all_students(md: dict):
    all_stud = ''
    for k, v in md.items():
        all_stud += k + ': '
        for k2, v2 in v.items():
            marks = ' '
            for i in v2:
                for j in i:
                    marks += j + ' '
            all_stud += k2 + ' - ' + str(marks) + ' '
        all_stud += '\n'

    print(all_stud)



