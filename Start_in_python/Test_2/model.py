journal_class = {}


def read_db(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data_lessons = file.readlines()
        for line in data_lessons:
            lessons = line.strip().split(';')
            lesson = lessons[0]
            pupils_marks = lessons[1].split(',')

            pupils = []
            marks = []
            for item in pupils_marks:
                pupil_marks = item.split(':')
                pupils.append(pupil_marks[0])

                marks.append(pupil_marks[1].split())


            for i, value in enumerate(marks):
                marks[i] = list(map(int, value))

            journal_class[lesson] = dict(zip(pupils, marks))


read_db('ttt.txt')

def save_changes(journal: dict, path: str):

    file_string = ''
    for i in journal.keys():
        file_string += i + ';'
        for j in journal[i].keys():
            file_string += j + ':'
            for k in range(len(journal[i][j])):
                file_string += ' ' + str(journal[i][j][k])
            file_string = file_string + ','
        file_string = file_string[:-1] + '\n'
    file_string = file_string[:-1]
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(file_string)

save_changes(journal_class,'ttt.txt')
