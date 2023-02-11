
# с целыми

# numbers = 'dfdf45678945fdf'
# number = ''
#
# for i in numbers:
#     if i.isdigit():
#         number += i
#
# print(number)
#
# numbers = 'dfdf45678945fdf'
# sum = 0
#
# for i in numbers:
#     if i.isdigit():
#         sum += int(i)
#
# print(sum)

# с вещественными. Превращаем строки из вещественных чисел в реальные
# вещественные или целые числа

# variable = '2.3 + 3 + 5.1'
# variable = variable.split(' + ')
# print(variable)
#
# num_list = []
#
# for i in variable:
#     if float(i) == int(float(i)):
#         num_list.append(int(i))
#     else:
#         num_list.append(float(i))
#
# print(num_list)

# типы данных
# пример конвертации строки в список

# text = 'Я вот такой молодец'
# print(list(text))
# new_text = text.split(' ')
# print(new_text)
# print(type(text))
# print(type(new_text))

# my_list = [1,'2',[3,3,3],4,5,6,7]
# my_tuple = (1,2,3,4,5,6,7)
# my_set = {1,2,3,4,5,6,7}
# my_dict = {'one': 1, 'two': 2, 'three': 3}

# копируем список

# a = [[1,2,3], [4,5,6]]  # когда у нас список списков, то чтобы указать индекс конкретного элемента нужно обращаться
#                         # сначала к списку, а затек эллемент. К примеру a[0][2] это будет элемент 3
#                         # если нам нужно скопировать матрицу, то в самом начале записываем
#                         # from copy import deepcopy
# a.append('jjj')
# b = a.copy()
# b.reverse()
# print(b)
# в случае описанном вверху, при изменении изначального списка, будет менять и список в пременной b,
# так как мы в переменную b записали ссылку первого списка переменнаая a.

# from copy import deepcopy
# a = [[1,2,3], [4,5,6]]
#
# b = deepcopy(a)
# a[0][2] = 'GGG'
#
# b.append('aaaa')
# b.append('ffff')
# print(a)
# print(b)
# а вот в данном случае, мы полностью копируем список, а не его копию, так что менять содержимое можно в обоих списках
# независимо друг от друга. Но тут уже будет не просто copy, а deepcopy

# срезы
my_list = [1,'2',[3,3,3],4,1,1,1,5,6,7,1]

# print(my_list[0:3])
# print(my_list[1:3])
# print(my_list[:3])
# print(my_list[3:])
# print(my_list[::-1]) # перевернутый список

# print(my_list)

# удаляем по конкретному индексу
# my_list.pop(1)
# print(my_list)

# удаляем по конкретному индексу
# del my_list[0]
# print(my_list)

# удаляем по первое вхождение символа или элемента
# my_list.remove(1)
# print(my_list)

# удаляем все вхождения символа или элемента
# new_list = [1,'2',[3,3,3],4,1,1,1,5,6,7,1]
# for i in new_list:
#     if 1 in new_list:
#         new_list.remove(1)
# print(new_list)

# тоже самое только через while
# while True:
#     if 1 in new_list:
#         new_list.remove(1)
#     else:
#         break
# print(new_list)

# print(my_list)
# element = my_list.pop(3) # как бы выдергиваем элемент из нашего списка
#                          # и записываем элемент в новую переменную
# print(element)
# print(my_list)
# my_list.append(element)
# print(my_list)
print(my_list)
my_list.insert(0,-9) # первая цифра это позиция, вторая это новый элемент, который мы хотим добавить
print(my_list)


