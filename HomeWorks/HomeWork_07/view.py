def main_menu():
    print('Главное меню')
    menu_list = ['Открыть файл',
                 'Показать все контакты',
                 'Найти контакт',
                 'Изменить контакт',
                 'Создать контакт',
                 'Удалить контакт',
                 'Сохранить файл',
                 'Выход'
                 ]

    for i in range(len(menu_list)):
        print(f'\t{i + 1}.{menu_list[i]}')
    while True:
        user_input = int(input('Введите команду :> '))
        if user_input < 1 or user_input > 8:
            print('Такого пункта нет, пожалуйста, выберите верный пункт')
            continue
        else:
            break
    return user_input
def show_all(db: list):
    if db_success(db):
        for i, item in enumerate(db):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in item.values():
                print(f'{v}', end=' ')
            print()
def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False
def exit_program():
    print('Завершение программы')
    exit()
def create_contact(db: list):
    if db_success(db):
        print('Создание нового контакта.')
        new_contact = dict()

        new_contact['lastname'] = input('\tВведите фамилию >: ')
        new_contact['firstname'] = input('\tВведите имя >: ')
        new_contact['phone'] = input('\tВведите номер телефона >: ')
        new_contact['comment'] = input('\tВведите комментарий >: ')
        db.append(new_contact)
        return db
def search_contact(db: list):
    user_choice = None
    while True:
        print('Как вы будете искать?\n'
              '\t1. Если по фамилии выбирите - 1\n'
              '\t2. Если по имени выбирите - 2\n'
              '\t3. Если по номеру выбирите - 3\n'
              '\t4. Если по комментарию выбирите - 4\n'
              )
        user_choice = int(input('Введите число >: '))
        if user_choice > 0 and user_choice <= 4:
            break
        else:
            print('Такого варианта нет. Выберите вариант от 1 до 4')
            continue
    d = {'1': 'Такого контакта в базе нет'}
    if user_choice == 1:
        lastname = input('\tВведите фамилию >: ')
        result = next((x for x in db if x['lastname'] == lastname), d)
        return result
    elif user_choice == 2:
        firstname = input('\tВведите имя >: ')
        result = next((x for x in db if x['firstname'] == firstname), d)
        return result
    elif user_choice == 3:
        phone = input('\tВведите номер >: ')
        result = next((x for x in db if x['phone'] == phone), d)
        return result
    elif user_choice == 4:
        comment = input('\tВведите оставленный комментарий >: ')
        result = next((x for x in db if x['comment'] == comment), d)
        return result
    print()
def show_result(db: list):
    if db_success(db):
        our_contact = search_contact(db)
        for v in our_contact.values():
            print(f'{v}', end=' ')
        print()
def support_show_all(db: list):
    for i, item in enumerate(db):
        user_id = i + 1
        print(f'\t{user_id}', end='. ')
        for v in item.values():
            print(f'{v}', end=' ')
        print()
def del_contact(db: list):
    if db_success(db):
        all_contacts = support_show_all(db)
        print('Какой контакт собираетесь удалять?')
        user_choce = int(input('Выбирите номер данного контакта :> '))
        db.pop(user_choce - 1)
        return db
def change_contact(db: list):
    if db_success(db):
        our_contact = search_contact(db)
        d = {'1': 'Такого контакта в базе нет'}
        while True:
            # our_contact = search_contact(db)
            if our_contact == d:
                print('Такого контакта в базе нет')
                break
            else:
                print('Такой контакт в базе есть: ')
                for i in our_contact.values():
                    print(f'{i}', end=' ')
                print()
                print('Что хотите изменить?\n'
                      '\t1. Если фамилию выберите - 1\n'
                      '\t2. Если имя выберите - 2\n'
                      '\t3. Если номер выберите - 3\n'
                      '\t4. Если комментарий выберите - 4\n'
                      )
                user_choice = int(input('Введите число >: '))
                if user_choice == 1:
                    our_contact['lastname'] = input('\tИзмените фамилию >: ')
                    return our_contact
                elif user_choice == 2:
                    our_contact['firstname'] = input('\tИзмените имя >: ')
                    return our_contact
                elif user_choice == 3:
                    our_contact['phone'] = input('\tИзмените номер >: ')
                    return our_contact
                elif user_choice == 4:
                    our_contact['comment'] = input('\tИзмените комментарий >: ')
                    return our_contact
                break































