# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
# библиотеки Random для и получения случайного int

import random

# my_list = [1, 2, 3, 4, 5, 6, 7]                       # вручную введенный список
my_list = [random.randint(-10, 10) for i in range(7)]   # рандомно созданный список
copy_list = my_list[:]                                  # копия списка

for i in range(len(my_list)):
    random_num = random.randint(0, (len(my_list)) - 1)
    copy_list[i], copy_list[random_num] = copy_list[random_num], copy_list[i]

print(f'Наш изначальный список -> {my_list}')
print()
print(f'Наша перемешанная копия -> {copy_list}')

