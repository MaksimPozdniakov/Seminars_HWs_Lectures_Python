# Задайте список из n чисел последовательности (1 + 1/n)^n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input('Введите число последовательности: '))
my_list = []
for n in range(1, number + 1):
    result = (1 + 1/n)**n

    if result - int(result) == 0:
        result = int(result)

    my_list.append(round(result, 2))

print(my_list)
print(sum(my_list))

