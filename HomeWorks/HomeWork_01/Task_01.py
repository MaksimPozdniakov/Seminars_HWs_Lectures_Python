# Задача №1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

day_week = int(input('Введите номер дня недели: '))

if day_week > 0 and day_week <= 5:
    print('Это будний день ')
elif day_week > 5 and day_week <= 7:
    print('Это выходной')
else:
    print('Такого дня недели нет!')

