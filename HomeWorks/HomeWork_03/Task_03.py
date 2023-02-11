# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

# my_float_list = [1.1, 1.2, 3.1, 5, 10.01]
my_float_list = [round(random.uniform(2, 5), 2) for i in range(4)]
new_list = []


for i in my_float_list:
    if isinstance(i, float):
        new_list.append(i % 1)


result = round(max(new_list) - min(new_list), 2)
print(f'Список вещественных чисел: {my_float_list}')
print(f'Разница между максимальной и минимальной дробной частью: {result}')






