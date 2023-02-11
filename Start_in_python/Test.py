# my_number = float(input('Введите число: '))
# def tttt():
#     my_number = 0.56
#     str_my_number = str(my_number)
#     list_my_number = list(str_my_number)
#     sum = 0
#
#     for i in list_my_number:
#         if i == '.':
#             list_my_number.remove('.')
#
#     for i in list_my_number:
#         sum += int(i)
#     return sum
#
# sum = tttt()
# result = str(sum)


# with open('text text.txt', 'w', encoding='UTF-8') as sum:
#     sum.write('Первый результат: ')
#     sum.write(result)

# data = open('text text.txt', 'r', encoding='UTF-8')
# result_1 = data.readline()
# print(result_1)
# print(type(result_1))

# with open('text.txt', 'r', encoding='UTF-8') as data:
#     result_1 = data.readline()
#     print(result_1)


# d = [{'lastname': 'Иванов', 'firstname': 'Иван', 'phone': '67809', 'comment': 'рабочий'},
#      {'lastname': 'Смирнов', 'firstname': 'Андрей', 'phone': '123456', 'comment': 'рабочий'}]
#
# result = next(x for x in d if x["lastname"] == "Иванов")
# print(result)
#
# result['lastname'] = "Cbljhjd"
# print(result)






# any([True for i, j in d[i].items() if j == "лом"])

# lstdict = [
#         { "name": "Klaus", "age": 32 },
#         { "name": "Elijah", "age": 33 },
#         { "name": "Kol", "age": 28 },
#         { "name": "Stefan", "age": 8 }
# ]
# print(next(x for x in lstdict if x["name"] == "Klaus"))
# print(next((x for x in lstdict if x["name"] == "David"), 'Такого контакта нет'))

# listOfDicts = [
#      { "name": "Tommy", "age": 20 },
#      { "name": "Markus", "age": 25 },
#      { "name": "Pamela", "age": 27 },
#      { "name": "Richard", "age": 22 }
# ]
# result = list(filter(lambda item: item['name'] == 'ddd', listOfDicts))
# if result:
#     print(result)
# else:
#     print('No')

# lstdict = [
#         { "name": "Klaus", "age": 32 },
#         { "name": "Elijah", "age": 33 },
#         { "name": "Kol", "age": 28 },
#         { "name": "Stefan", "age": 8 }
#        ]
#
# print([x for x in lstdict if x['name'] == 'Kol'][0])

# d = {'1': ['5','3','5'], '2': ['5','2','5'], '3': ['5','5','5','5']}
# n = input('input: ')
# m = input('input mark: ')
# d[n].append(m)
# print(d)

# d = {'Русский язык': {'Иванов Иван': ['5', '4', '3'], 'Петрова Елена': ['5', '4', '5']},
#      'Русская литература': {'Иванов Иван': ['3', '3', '4', '3', '5'], 'Петрова Елена': ['2', '4', '5', '3']},
#      'Математика': {'Иванов Иван': ['4', '4', '3', '5'], 'Петрова Елена': ['4', '4', '4', '5']}}

# надо Русский язык;Иванов Иван|5 4 3|Петрова Елена|5 4 5
#      Русская литература;Иванов Иван|3 3 4 3 5|Петрова Елена|2 4 5 3
#      Математика;Иванов Иван|4 4 3 5|Петрова Елена|4 4 4 5


# l= ''
# file_string = ''
# for sub in d.keys():
#      file_string += sub + ';'
#
#      for names in d[sub].keys():
#           file_string += names + '|'
#
#           for marks in range(len(d[sub][names])):
#
#                file_string += str(d[sub][names][marks]) + ' '
#
#           file_string = file_string + '|'
#      file_string = file_string[:-1] + '\n'
# file_string = file_string[:-1]
#
#
# print(file_string)
#
# l = ['4435995', '4435995']
#
# marks2 = ''
# for i in l:
#      marks = ''
#      for j in i:
#           marks += j + ' '
#      marks2 += marks + ' '
# print(marks2)

# def fff():
#
#     d = {'Иванов Иван': ['443553'], 'Петрова Елена': ['4445354']}
#     return d
#
# def add_student():
#     subject = fff()
#     new_student = input('Введите фамилию и имя новуго ученика: ')
#     new_marks = []
#     subject[new_student] = new_marks
#     return subject
#
# res = add_student()
# print(res)

p = 8

d = {342216687: {'change_total': 188}}
u = 'change_total'

for k, v in d.items():
    for i in v.keys():
        if i == u:
            v[i] -= p



# d = {'candy_total': 188, 'change_total': 188, 'level': 'hard'}
# d['change_total'] -= k


print(d)






