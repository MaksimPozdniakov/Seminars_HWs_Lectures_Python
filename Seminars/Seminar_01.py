# Задача №1. Вывод от 0 до n.
# n = int(input('В: '))
# i = 1
# while i <= n:
#     if i != 0:
#         print(i)
#     i += 1

# 2. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# num1 = int(input('num1 = '))
# num2 = int(input('num2 = '))
# step = 2
# result = num1 ** step
# if num2 == result:
#     print('True')
# else:
#     print('False')

# Задача №3. 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

list1 = [1, 4, 8, 7, 5]
list2 = [78, 55, 36, 90, 2]
print ("min number is ", min(list1))
print ("max number is ", max(list1))
print ("min number is ", min(list2))
print ("max number is ", max(list2))

# альтернативный вариант
my_list = []  # таким образом мы в ручную заполняем список
for i in range(5):
    number = int(input('Введите число '))
    my_list.append(number)
print(my_list)

my_max = my_list[0]

for item in my_list:  # так мы обращаемся к самим элементам, а не к индексам
    if my_max < item:
        my_max = item
print(my_max)

# for i in range(len(my_list)):    # так мы обращаемся к индексам
#     my_list[i] = 6

