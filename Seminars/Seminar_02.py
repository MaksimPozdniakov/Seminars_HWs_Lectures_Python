# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

# number = int(input('Введите целое число: '))
#
# for degree in range(number):
#     print((-3)**degree)

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число: '))
# my_dict = {}
# for i in range(1, n+1):
#     my_dict[i] = 3 * i + 1
#
# print(my_dict)

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
# вхождений одной строки в другой.

# first_string = 'Hello World'
# second_string = 'l'
# count = 0
# for i in range(len(first_string) - len(second_string)):
#     if first_string[i] == second_string[0]:
#         flag = True
#         for j in range(1,len(second_string)):
#             if second_string[j] != first_string[i+j]:
#                 flag = False
#         if flag:
#             count += 1
# print(count)

# def count_strings(first_string, second_string):
#     count = 0
#     i = -1
#     while True:
#         i = first_string.find(second_string, i+1)
#         if i == -1:
#             return count
#         count += 1
# print(count_strings('Hello World', 'l'))

# Алгоритм, который считает сколько букв из одной строки встречается в другой строке
# first_string = 'Hello World'
# second_string = 'World hello'
# print(first_string, second_string, sep='\n')
# my_list1 = []
# my_list2 = []
# count = 0
#
# for i in first_string:
#     if i != ' ':
#         my_list1.append(i)
# for j in second_string:
#     if j != ' ':
#         my_list2.append(j)
#
# for i in my_list1:
#     if i in my_list2:
#         count = count + 1
#
# print(count)

#
# import random
# n = int(input('Введите число: '))
# my_list = []
# for i in range(n):
#     my_list.append(random.randint(-100,100))
#
# print(my_list)

# My seminar

# Задача №1. Напишите программу, которая будет на входе принимать
# число N и выводить числа от -N до N

# number = int(input('Введите число: '))
#
# if number > 0:
#     for i in range(-number, number + 1):
#         if i != number:
#             print(i, end=', ')
#         else:
#             print(i)
# else:
#     for i in range(number, (-number) + 1):
#         if i != abs(number):
#             print(i, end=', ')
#         else:
#             print(i)

# еще один вариант:
# number = int(input('Введите целое число: '))
# if number > 0:
#     for num in range(-number,number+1):
#         print(num, end = ', ')
# elif number < 0:
#     for num in range(number,(-number) + 1, 1):
#         print(num, end=', ')
#
# # еще один вариант от Стена:
# number = int(input('Введите целое число: '))
# my_list = []
#
# for i in range(-number, int(number+abs(number)/number), int(abs(number)/number)):
#     my_list.append(i)
#
# print(*my_list, sep=', ')



# Задача №2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# number = float(input('Введите число: '))
#
# if number != int(number):
#     number = (abs(number) * 10) % 10
#     print(int(number))
# else:
#     print('Это целое число')

# альтернативный вариант решения
# number = float(input('Введите число: '))
# my_list = []
# result = 0
# while number > 10:
#     number = number // 10
# else:
#     number = number * 10
#     result = number % 10
#
# print(round(result))

# альтернативный вариант решения
# number = input('V')
# number = number.split('.')
# print(number)
# if len(number) > 1:
#     print(number[1][0])
# else:
#     print('Число целое')

# альтернативный вариант решения от Ёды
# n = float(input('Enter number: '))
# if(int(n) == n):
#     print('no')
# else:
#     print(int(abs(n) * 10) % 10)

# альтернативный вариант решения от Стена
# n = float(input('Enter number: '))
#
# if n != int(n):
#     print(int(abs(n) * 10) % 10)
# else:
#     print('Нет дробной части')
































