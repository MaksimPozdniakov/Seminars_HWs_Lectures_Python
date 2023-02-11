# Введение
# 1)
# string = '1 2 3 4 5 6 7 8 9'
# string = string.split()
# print(string)

# for i in range(len(string)):
#     string[i] = int(string[i])
# print(string)

# 2) map
# def cube(x):
#     return x**2

# string = list(map(int, string))
# string = list(map(cube, string))
# print(string)

# тоже самое только в одну строчку
# string = list(map(cube, list(map(int, string))))
# print(string)

# тоже самое только в одну строчку
# string = list(map(cube, list(map(int, string.split()))))
# print(string)

# тоже самое только в одну строчку через lambda без функции def
# string = list(map(int, string.split()))
# string = list(map(lambda x: x**2, string))
# print(string)

# 2) filter
# string = list(map(int, string.split()))
# string = list(filter(lambda x: x%2 == 0, string))
# print(string)

# 3) enumerate

# string = string.split()
# клас метод реш
# for item in string:
#     print(item)

# клас метод реш
# for i in range(len(string)):
#     print(string[i])

# через enumerate
# for i, item in  enumerate(string):
#     print(f'Индекс = {i}, элемент = {item}')

# 4) zip

# letters = 'a b c d e f g'
# nums = '1 2 3 4 5 6 7'
# nums = nums.split()
# letters = letters.split()
#
# new_list = list(zip(nums, letters))
# print(new_list)

# 5) всякое полезное

# calc = {'Сложение': lambda x, y: x + y}
# print(calc.get('Сложение')(4, 5))

# жуть
# string = '234 234 234543 6346 545 6745'
# print(list(filter(lambda x: x%2 == 0, list(map(int, string.split())))))


# Задача №1. Дана последовательность чисел. Получить список уникальных
# элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# data = [1, 2, 3, 5, 1, 5, 3, 10]

# my_dict = dict()
# for i in range(len(data)):
#     my_dict[data[i]] = my_dict.get(data[i], 0) + 1
# print(my_dict)
#
# new_data = [x[0] for x in my_dict.items() if x[1] == 1]
# print(new_data)


# еще один вариант решения
# for i in arr:
#         cnt_dict[i] = 1 if (i not in cnt_dict) else cnt_dict[i] + 1

# еще один вариант решения
# my_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(my_list)

# от Стоуна
# my_dict = {}
# for item in data:
#     my_dict[item] = my_dict.get(item, 0) + 1
# for key, value in my_dict.items():
#     if value == 1:
#         print(key)

# от Стоуна
# print([x for x in data if data.count(x) == 1])

# еще от Ёды
# new_data = list(filter(lambda x: data.count(x) == 1, data))

# еще от Ёды
# proverka = lambda x: data.count(x) == 1
# new_data = list(filter(proverka, data))
# print(new_data)

#  Задача №2. Напишите прграмму вычисления арифметического выражения заданного строкой.
#  Используйте +,-,/,*. Приоритет операций стандартный.

# Пример:
# 2+2=4;
# 1+2*3=7
# 1-2*5=-5

# data_1 = '2+2'
# data_2 = '1+2*3'
# data_3 = '3-2*5'
# data_4 = '-2*3 - 4*5'
#
# data = data_4.replace('+', ' + ').replace('-', ' - ')\
#     .replace('/', ' / ').replace('*', ' * ').replace('- ', '-')
# data = data.split()
#
# oper = {
#     '+': lambda x, y: int(x) + int(y),
#     '-': lambda x, y: int(x) - int(y),
#     '/': lambda x, y: int(x) / int(y),
#     '*': lambda x, y: int(x) * int(y),
# }
#
# def calc(data: list) -> int:
#     for i in range(len(data) - 1):
#         if data[i] in '*/':
#             operation = data[i]
#             left = data[i-1]
#             right = data[i+1]
#             res = oper[operation](left, right)
#             # print(f'Рез операции {left} {operation} {right} = {res}')
#             return data[:i-1] + [str(res)] + data[i+2:]
#
#     for j in range(len(data) - 1):
#         if data[j] in '+-' and j != 0:
#             operation = data[j]
#             left = data[j-1]
#             right = data[j+1]
#             res = oper[operation](left, right)
#             # print(f'Рез операции {left} {operation} {right} = {res}')
#             return data[:j-1] + [str(res)] + data[j+2:]
#
# for item in oper.keys():
#     while item in data:
#         data = calc(data)
#
# print(data[0])

# вариант от Стоуна



























