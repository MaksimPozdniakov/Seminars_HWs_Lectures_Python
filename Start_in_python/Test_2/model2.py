main_dict = {}


def open_file(path: str):
    global main_dict
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        new_list = []
        for line in data:
            items = line.strip().split(';')
            new_list.append(items)

        for i, item in enumerate(new_list, 1):
            pupiles = item[1].split('|')
            names = [pupiles[j] for j in range(0, len(pupiles), 2)]
            marks = [pupiles[n] for n in range(1, len(pupiles), 2)]

            marks2 = []
            for j in marks:
                marks2.append(j.split(' '))

            new_dict = dict(zip(names, marks2))
            main_dict[item[0]] = new_dict
    print(main_dict)

open_file('kkk.txt')

def save_changes(path: str, md: dict):
    file_string = ''
    for i in md.keys():
        file_string += i + ';'
        for j in md[i].keys():
            file_string += j + '|'
            for k in range(len(md[i][j])):
                file_string += str(md[i][j][k])
            file_string = file_string + '|'
        file_string = file_string[:-1] + '\n'
    file_string = file_string[:-1]
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(file_string)

save_changes('kkk.txt', main_dict)
