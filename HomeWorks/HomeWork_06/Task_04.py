# Задача №4. Есть кортеж t = 1, 2, 3, 5, 8, 15, 23, 38, нужно отсортировать по положительным
# цифрам и возвести их во второю степень. Вывесте список кортежей с парами чисел из
# обычного положительного и его варианта в степени 2

# старое решение

# t = 1, 2, 3, 5, 8, 15, 23, 38
# my_list = list(t)
#
# def kvadr(my_list: list):
#     my_list1 = []
#
#     for i in range(1, len(my_list)):
#         if my_list[i] % 2 == 0:
#             result = my_list[i]**2
#             my_list1.append((my_list[i], result))
#     return my_list1
#
# result = kvadr(my_list)
# print(result)

# новое решение

t = 1, 2, 3, 5, 8, 15, 23, 38
my_list = list(t)

res = list(filter(lambda x: x % 2 == 0, my_list))
new_res = list(map(lambda x: x**2, res))
result = list(zip(res, new_res))
print(result)


