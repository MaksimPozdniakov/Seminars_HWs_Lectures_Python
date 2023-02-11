# enumerate

# a = [1, 2, 3, 4, 5, 6]
# b = 'hello'
# c = ('apple', 'banana', 'mango')
# d = {'1': 'one', '2': 'two', '3': 'three'}
# cities = {'Las Vegas', 'Paris', 'Moscow'}
#
# # print(list(enumerate(a, 1)))
#
# for index, value in enumerate(a):
#     a[index] += 1
# print(a)

# lambda

# def f(a):
#     return a**2
# print(f(2))
#
# new_f = lambda a: a**2
# print(new_f(2))

# f = lambda: 'Hello'
# print(f())

# def f(a):
#     if a > 0:
#         return('pozitiv')
#     else:
#         return('negativ')
# a = f(2)
# print(a)
#
# a_1 = lambda a: 'pozitiv' if a > 0 else 'negativ'
# print(a_1(2))

# def f(a):
#     return a%10
#
# a = [11, 20, 35, 44, 59, 68]
#
# a.sort(key = f)
# print(a)

# a = [119, 20, 35, 44, 59, 68]
#
# a.sort(key = lambda x: x%10)
# print(a)

# def f(a, b):
#     return lambda x: x*a+b
#
# graf1 = f(2, 3)
# print(graf1(2))

# List comprehension

import random
#
# a = [random.randint(1, 10) for i in range(1,9)]
# print(a)

# a = [i for i in range(9)]
# print(a)

# a = [i**2 for i in range(9)]
# print(a)

# a = [i for i in 'Hello']
# print(a)
#
# a = [i*5 for i in 'Hello']
# print(a)

# a = [ord(i) for i in 'Hello']
# print(a)

# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# a = [elem for elem in a if elem % 2 == 0 and elem % 3 == 0]
# print(a)

# a = input().split()
# a = [int(i) for i in a]
# print(a)

# a = 4
# b = 4
# li = [[0] * a for i in range(b)]
#
# li[0][3] = 100
# for i in li:
#     print(i)

# li = [(i, j) for i in 'ABC' for j in [1, 2, 3]]
# print(li)

# li = [i*j for i in [1,2,3,4,5] for j in [1,2,3] if i*j>10]
# print(li)

# li = input('Введите числа: ').split()
# li = [int(i)**3 for i in li]
#
# print(li)

# li = [('Сидоров', 1995),
#       ('Петров', 2005),
#       ('Росторгуев', 1997),
#       ('Котенков', 1996)
# ]
# # print(li)
# li1 = [elem for elem in li if elem[1] > 2000]
# print(li1)

# s = '4f8f7t4g5f8d4d58gf8f4d2'
# b = [int(i) for i in s if i.isdigit()]
# print(b)

# s = '4f8f7t4g5f8d4d58gf8f4d2'
# b = [i for i in s if i.isalpha()]
# print(b)
# import random
# a = 4
# b = 4
# s = [[random.randint(1,9) for j in range(a)] for i in range(b)]
#
# for i in s:
#       print(i)
# print()

# f = [s[i][j] for i in range(a) for j in range(b) if i == j]
# print(f)

# k = [s[2][j] for j in range(b)]
# print(s[2])
# print()
# print(k)

# u = [s[i][2] for i in range(a)]
# print(u)

# a = 7
# b = 7
# f = [[i * j for i in range(1, a)] for j in range(1, b)]
# for i in f:
#       print(i)

# Выражения-генераторы

# f = [1,23,2,34,45,56,67]
# f = (i for i in range(1, 8))
#
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


# функция генератор

# def genf():
#     for i in [43,54,65]:
#         yield i
# s = genf()
# print(next(s))
# также мы можем пробежать по нашей функции через цикл for
# for i in genf():
#     print(i)

# def genf():
#     s = 7
#     for i in [43,54,65]:
#         yield i
#         print(s)
#         s = s * 10 + 7
#
# f = genf()
# print(next(f))
# print(next(f))
# print(next(f))

# нахождение факториала через классическую функцию
# def fact(n):
#     pr = 1
#     result = []
#     for i in range(1, n+1):
#         pr = pr * i
#         result.append(pr)
#     return result
# res = fact(10)
# print(res)

# а теперь  через генератор функции
# def factor_gen(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr = pr * i
#         yield pr
#
# for i in factor_gen(10):
#     print(i, end=' ')

# map()


# l = [-1, 2, -3, 4, 5]
# b = list(map(abs, l))
# print(b)
#
# l_2 = [abs(i) for i in l]
# print(l_2)
#
# def func(x):
#     return x**2
#
# b = list(map(func, l))
# print(b)
#
# a = ['hello', 'hi', 'good morning']
# b = list(map(str.upper, a))
# print(b)

# a = ['hello', 'hi', 'good morning']

# b = list(map(lambda x: x[::-1], a))
# print(b)
# def func(x):
#     result = x[::-1]
#     return result
# c = list(map(func, a))
# print(c)
#
# k = [i[::-1] for i in a]
# print(k)

# p = list(map(lambda x: x+'!', a))
# print(p)
#
# y = list(map(int, input().split()))
# print(y)

# c = (lambda x: x**3)(10)
# print(c)

# filter

# a = [1, 23, 34, 4556, 345, 34, 324, 7, 6, 5, 43]
# def f(n):
#     return n > 10

# res = list(filter(f, a))
# print(res)
# тоже самое только через генератор списка

# res2 = [i for i in a if i > 9 and i < 100]
# print(res2)

# b = [1,2,3,4,5,6,7,0,0,0,'',' ']
# res3 = list(filter(None, b))
# print(res3)

# c = ['Привет', 'Нет', 'Да', 'как']
# res4 = list(filter(lambda x: len(x) <= 3, c))
# print(res4)

# t = '345567hdjfbdjkdfb567543'
# res5 = list(filter(str.isdigit, t))
# print(res5)

# my_dict = {
#     'moscow': 800,
#     'danmark': 700,
#     'england': 300,
#     'Dochland': 100
# }
#
# res6 = list(filter(lambda x: my_dict[x] > 500, my_dict))
# print(res6)


# zip

# a = [5, 6, 7, 8]
# b = [100, 200, 300, 40]
# c = 'abcd'
# for i in range(4):
#     print(a[i], b[i])

# res = list(zip(a, b, c))
# print(res)
#
#
# for t1, t2, t3 in zip(a, b, c):
#     print(t1, t2, t3)
# res = zip(a, b, c)
# col1, col2, col3 = zip(*res)
# print(col1, col2, col3)



# это мой вариант решения
t = 1, 2, 3, 5, 8, 15, 23, 38
my_list = list(t)

def kvadr(my_list: list):
    my_list1 = []

    for i in range(1, len(my_list)):
        if my_list[i] % 2 == 0:
            result = my_list[i]**2
            my_list1.append((my_list[i], result))
    return my_list1

result = kvadr(my_list)
print(result)



res = list(filter(lambda x: x % 2 == 0, my_list))
new_res = list(map(lambda x: x**2, res))
result = list(zip(res, new_res))
print(result)

res2 = [i**2 for i in my_list if i % 2 == 0]
res3 = [i for i in my_list if i % 2 == 0]
print(list(zip(res3, res2)))

