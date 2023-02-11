# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input('Введите вещественное число: '))
str_num = str(number)
list_num = list(str_num)

count_sum = 0

for i in list_num:
    if i == '.':
        list_num.remove('.')

for i in list_num:
    count_sum += int(i)

print(f'Сумма цифр в нашем числе -> {count_sum}')

