# 1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

#num = int(input("Введите число: "))
#count = num + 2
#print("Результат", count)

# 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых.
# И просите ввести заново.
# первый вариант решения
# num = int(input("Введите число: "))
#
# while num <= 0 or num >= 10:
#    print("Вы ввели неверное число!")
#    num = int(input("Введите число, которое больше 0 и меньше 10: "))
# # print("Вы ввели подходящие число! Число",num, "во второй степени будет ровняться", num * num)
# print("Вы ввели подходящие число! Число",num, "во второй степени будет ровняться", num ** 2)

# второй вариант решения

# while True:
#     num = int(input("Введите число "))
#     if num > 0 and num < 10:
#         print(num ** 2)
#         break
#     else:
#         print("Число должно быть > 0 и < 10")


# 3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст
# и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

# name = input("Введите свое имя: ")
# second_name = input("Введите свою фамилию: ")
# age = int(input("Укажите свой возраст: "))
# weight = int(input("Укажите свой вес: "))
#
# if age < 30 and weight > 50 and weight < 120:
#     print("Пациент в хорошем состоянии ")
# elif age > 30 and age < 40 and (weight < 50 or weight > 120):
#     print("Пациенту требуется заняться собой ")
# elif age > 40 and (weight < 50 or weight > 120):
#     print(name, second_name, age, "Год,", "Вес", weight, "- Пациенту требуется врачебный осмотр ")

# Кусочек следующего урока

# 1. Написать программу, которая будет выводить в терминал победителей

# top5 = "Первые 5 мест в соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов"
# start = top5.find("1") # тут мы указываем какой символ мы хотим найти, чтобы определить начало нучной нам информации
# end = top5.find("4") # это конец
# top3 = top5[start: end] # тут мы указываем, что нам нужен интервал, который начинается в start и идет до end
#
# result = "Поздравляем {} с успехом!".format(top3.upper()) # делаем вывод через format, дополнительно через upper() мы
#                                                           # вывод делаем с верхнему регистра
# print(result)

# 2. Задача про победителей соревнования по python
# первый вариант решения (простой)
# player1 = input("Кто занял 5 место? ")
# player2 = input("Кто занял 4 место? ")
# player3 = input("Кто занял 3 место? ")
# player4 = input("Кто занял 2 место? ")
# player5 = input("Кто занял 1 место? ")
# print("В соревновании учавствовали {}, {}, {}, {}, {}".format(player1,player2,player3,player4,player5))
#
# print("Победители {},{},{}".format(player5,player4,player3))

# второй вариант решения (правильный)
# print("Соревнования по python")
# count = int(input("Введите количество игроков: "))
# i = count
# members = []
# while i > 0:
#     name = input("Кто занял {} место ".format(i))
#     members.append(name)
#     i-=1
# print("В соревнованиях учавствовали:", members)
#
# members.reverse() # тут мы первернули наш массив
# result = members[:3] # тут мы сделали срез, чтобы выделить тольок первые 3 места
# result = "Победители: {}. Поздравляем!" .format(result)
# print(result)

# while

# friends = ["Ron", "Kate", "Nik"]
# friend_name = "Maksim"
# 1. список
# i = 0
# while i < len(friends):
#     friend = friends[i]
#     print(friend)
#     i+=1
# 2. строка
# i = 0
# while i < len(friend_name):
#     letter = friend_name[i]
#     print(letter)
#     i+=1

# for
# 1. список
# for friend in friends:
#     print(friend)
# 2. строка
# for letter in friend_name:
#     print(letter)

# продолжаем работать с циклами (функция range)

# print(list(range(1,1000,2))) # одной строкой кода выводим нечетные числа в заданном нами диапазоне

# for number in range(1,1000,2): # то же самое, только через цикл for
#     print(number)

# тип данных словарь

# friend = {
#     'name': 'Max',
#     'age': 23
# }
#
# print(friend)
#
# print(friend['age'])
#
# friend['has_car'] = True # добавили ключ в наш словарь
# print(friend)
#
# del friend['age'] # удалили ключ из словаря
# print(friend)
#
# if 'age' in friend: # проверили на наличие ключа в словаря, в данном случае такого элемента в словаре нет
#     print('Есть возраст')
#
# if 'has_car' in friend:
#     print('Есть машина')

# перебор словаря

# friend = {
#     'name': 'Max',
#     'age': 23,
#     'has_car': True
# }

# по ключам
# for key in friend.keys():
#     print(key) # так мы получаем ключи
#     print(friend[key]) # так мы получаем значения

# for key in friend:
#     print(key) # так мы получаем ключи
#     print(friend[key]) # так мы получаем значения
# по значениям
# for val in friend.values():
#     print(val)

# пары ключ и значение
# for item in friend.items():
#     print(item)

# for key, val in friend.items():
#     print(key)
#     print(val)

# множества

# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow'] # сначала определили список(массив)
# print (cities)
#
# cities = set(cities) # тут мы преобразовали список во множество
# print (cities)
#
# cities = {'Las Vegas', 'Moscow', 'Paris'}
# print (cities)

# cities = {'Las Vegas', 'Moscow', 'Paris'}
# print(cities)
#
# # добавление элемента
# cities.add('Burma')
# print(cities)
#
# # удаление элемента
# cities.remove('Paris')
# print(cities)


# Задача: семейная пара собирается в отпуск
# каждый из супругов собирает в поездку вещи
# Макс взял эти
# max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# # Кейт взяла эти
# kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
#
# # какие вещи взяли супруги
# print(max_things|kate_things)
# # найти вещи которые повторяются
# print(max_things&kate_things)
# # какие вещи взял Макс, но не взяла Кейт
# print(max_things-kate_things)
# # какие вещи взяла Кейт, но не взял Макс
# print(kate_things-max_things)

# Задача  №1 Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# первый вариант решения
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
#
# for i in my_list_2:
#     while i in my_list_1:
#         my_list_1.remove(i)
# print(my_list_1)

# второй вариант решения
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
#
# for i in my_list_1[:]:          # благодаря срезу - это квадратные ковычки после my_list_1 мы как бы создаем копию
#                                 # данного списка и дальше уже работаем с ней. В данном случае срез обязательный, так
#                                 # как мы удаляем элементы из списка.
#     if i in my_list_2:
#         my_list_1.remove(i)     # тут мы уже работаем не с копией, а с оригинальным списком
#
# print(my_list_1)

# Задача №2 Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде,
# например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

# date = '02.11.2013'
#
# d, m, y = date.split('.')  # тут мы разделяем строчку на нужное количество на частей
# print(d, m, y)
#
# months = {                       # мы собираемся преобразовать эту строку в текстовый вид.
#     '01': 'января',             # Для этого нам потребуется словарь.
#     '11': 'ноября'
# }
# days = {                        # мы собираемся преобразовать эту строку в текстовый вид.
#     '01': 'перовое',            # Для этого нам потребуется словарь.
#     '02': 'второе'
# }
#
# result = f'{days[d]} {months[m]} {y} года.'
# print(result)

# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# my_list_2 = []
#
# for i in my_list_1:
#     if my_list_1[i] != my_list_1[i+1]:
#         value = my_list_1[i]
#         my_list_2.append[value]
#
# print(my_list_2)

# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# result = []
#
# for i in my_list_1:
#     if my_list_1.count(i) == 1:
#         result.append(i)
#
# print(result)


# Что выведет в консоль эта программа:
# list1 = ['hi', 'bro']
# list2 = list1
# list2.append('welcome')
# print(len(list1))

# Что выведет в консоль эта программа:
# b = 4
# a = 2
# print(a // b * a)

# Что выведет в консоль эта программа:
# s = "ur4"
# s += 'C'
# print(s[-1] + s[1] + s[-4] + s[2])

# Функции
# r = range(10)
# print(*r)

# Задача №1. Пользователь вводит 3 числа. Найти минимальное из них,
# максимальное из них, их сумму и вывести результат на экран.

# numbers = []
# for num in range(5):
#     num = int(input(f'Введите {num + 1} число: '))
#     numbers.append(num)
# print(numbers)
# # Найти минимальное из них
# print(min(numbers))
# # Найти максимальное из них
# print(max(numbers))
# # Найти их сумму
# print(sum(numbers))

# import random
#
# my_list = [random.randint(1, 100) for i in range(7)]
# print(my_list)
#
# print(len(my_list))

# Создание собственных функций
# def print_sep(sep, sep_len):
#     print(sep * sep_len)
#
# print_sep('-', 100)
# print_sep('*', 100)

# возвращаемое значение
# def print_sep(sep, sep_len):
#     return sep * sep_len
#
# sep = print_sep('-', 50)
# text = 'Hello {} Func {}'.format(sep, sep)
# print(text)

# def print_sep(say, who):
#     print(say, who)
#
# print_sep(say = 'Hello', who = 'Max')

# def print_sep(who, say = 'Hello'):
#     print(say, who)
#
# print_sep('Max')
# print_sep('Max', 'Hi')

# args, kwargs
# def print_sep(say, *args):
#     print(say, args)
#
# print_sep('Hi', 'Leo','Leo','Leo','Leo')
#
# def print_func(**kwargs):
#     for k,v in kwargs.items():
#         print(k, v)
#
# print_func(name = 'Leo', age = 20, has_car = True)

# Уроки со степика!

# separ = input('Разделитель: ')
# a, b, c = input('a= '), input('b= '), input('c= ')
#
# print(a,b,c, sep=separ)

# name = input()
# print('Привет {} !'.format(name)
















































