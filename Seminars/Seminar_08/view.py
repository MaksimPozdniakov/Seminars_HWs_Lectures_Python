def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Введите класс',
                '',
                '',
                '',
                '',
                '',
                ''
                ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
        user_input = int(input('Введи команду >: '))

        return user_input






