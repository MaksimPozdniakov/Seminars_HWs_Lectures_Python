class_dict = {}

def read_db(path: str):
    global class_dict
    with open(path, 'r', encoding='UTF-8') as file:
        class_list = file.readlines()
        class_db = []

        for line in class_list:
            pupiles_marks = line.strip().split('|')
            class_db.append(pupiles_marks)

        for i, item in enumerate(class_db):
            pupiles = item[1].split(';')

            names = [pupiles[j] for j in range(0, len(pupiles), 2)]
            marks = []
            for v in pupiles[1]:
                if v.isdigit():
                    marks.append(v)

            pupils_dict = dict(zip(names, marks))
            class_dict[item[0]] = pupils_dict



            
read_db('7A.txt')









