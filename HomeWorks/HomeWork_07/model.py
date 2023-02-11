db_list = []
def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)

def change_file(path: str, db: list):
    k = ''
    for i in db:
        t = ';'.join(i.values())
        t += '\n'
        k += t

    with open(path, 'w', encoding='UTF-8') as file:
        file.write(k)


