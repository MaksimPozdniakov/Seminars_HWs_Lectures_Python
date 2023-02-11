# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

#my_list = [2, 3, 4, 5, 6]
my_list = [2, 3, 5, 6]
new_list = []
size = (len(my_list) / 2)

for i in range(len(my_list)):
    if i < size:
        if i != ((len(my_list) - 1) - i):
            result = my_list[i] * my_list[(len(my_list) - 1) - i]
            new_list.append(result)
        else:
            new_list.append(my_list[i])

print(new_list)