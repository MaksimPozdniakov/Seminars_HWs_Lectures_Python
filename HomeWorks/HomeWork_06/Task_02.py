# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции
# с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# старое решение
# def Sum_Of_Elements(my_list):
#     sum = 0
#
#     for i in range(len(my_list)):
#         if i % 2 != 0:
#             sum += my_list[i]
#     print(sum)
#
# my_list = [2, 3, 5, 9, 3]
# Sum_Of_Elements(my_list)

# новое решение

from random import randint as ri

my_list = [ri(1, 10) for i in range(10)]
print(f'Наш сгенерированный спсок: {my_list}')

result = [y for x, y in enumerate(my_list) if x % 2 != 0]
print(f'Сумма элементов стоящих на нечетных позициях: {sum(result)}')


