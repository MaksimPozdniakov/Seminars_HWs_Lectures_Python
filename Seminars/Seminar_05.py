# Задача №1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

# по классике

# data = '1 2 3 4 5 6 8 9 10'
# data = [int(x) for x in data.split()]  # альтернативный вариант след строки
# new_data = list(map(int, data.split()))

# for i in range(len(new_data) - 1):
#     if new_data[i] + 1 != new_data[i+1]:
#         print(new_data[i] + 1)

# через lambda вариант 1

# res = list(filter(lambda i: not new_data[i] + 1 == new_data[i + 1], range(len(new_data) - 1)))
#
# for i in res:
#     print(new_data[i] + 1)

# # через lambda вариант 2 разобраться с выводом
# f = lambda data: ([data[i]-1 for i in range(0,len(data)) if data[i]-data[i-1] == 2]).pop()
# print(list(f))

# Задача №2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую
# последовательность. Порядок элементов менять нельзя. Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# мое решение

# l = [1, 5, 2, 3, 4, 6, 1, 7]
# result = []

# for i in range(len(l) - 1):
#     temp = []
#     temp.append(l[i])
#     for j in range(i + 1, len(l)):
#         if l[i] < l[j] and l[j] > l[j-1]:
#             temp.append(l[j])
#             i += 1
#     result.append(temp)
# print(result)

# от Стоуна

# data = [1, 5, 2, 3, 4, 6, 1, 7]
# result = []
# count = 0
# num1 = 1
# while count < len(data):
#     for i in range(len(data) - 1):
#         temp = []
#         temp.append(data[i])
#         cur_max = data[i]
#         for j in range(num1, len(data)):
#             if data[j] > cur_max:
#                 temp.append(data[j])
#                 cur_max = data[j]
#         if len(temp) > 1 and temp not in result:
#             result.append(temp)
#     count += 1
#     num1 += 1
# print(result)

# Задача №3. Напишите прграмму, удаляющую из текста все слова, содержащие "абв"

# первый вариант

# str1 = 'вбвпро пррара рарабв раощывDDDоралдоы лорыапабвлроап АБВ абВ'
# str2 = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), str1.split())))
# print(str2)

# второй вариант

# str1 = 'вбвпро пррара рарабв раощывDDDоралдоы лорыапабвлроап АБВ абВ'
# str1 = str1.split()
# t = 'абв'
# str2 = []
#
# for item in str1:
#     if not t.lower() in item.lower():
#         str2.append(item)
# print(' '.join(str2))

# доп вариант, сохраняем знаки припинания

# from string import punctuation
# str1 = 'вбвпро пррара рарабв раощывDDDоралдоы лорыапабвлроап АБВ? абВ'
# t = 'абв'
# str2 = []

# for x in punctuation:
#     str1 = str1.replace(x, ' ' + x + ' ')

# str1 = str1.split()

# for item in str1:
#     if not t.lower() in item.lower():
#         str2.append(item)
# res = ' '.join(str2)
# for x in punctuation:
#     res = res.replace(' ' + x, x)

# print(res)

















