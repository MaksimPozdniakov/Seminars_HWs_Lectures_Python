# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей нет
# data.close()

# with open('file.txt', 'w') as data:
# 	data.write('dfsdfsdfs')
# 	data.write('23123123')
# print(data)

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import previous
# print(previous.function_name(1))

# import previous as p
# print(p.function_name(1))

# Рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# my_list = []
# for e in range(1, 10):
#     my_list.append(fib(e))
#
# print(my_list)

# Кортежи

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

# Списки

import random
my_list = [random.randint(1, 10) for i in range(7)]
new_list = my_list.copy()
print(my_list)





