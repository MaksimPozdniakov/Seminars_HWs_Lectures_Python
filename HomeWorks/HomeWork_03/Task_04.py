# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = 45
number = int(input('Введите число: '))
num = number
my_list = []

while num > 0:
    result = num % 2
    num = num // 2
    my_list.append(str(result))

my_list.reverse()
new_num = int(''.join(my_list))
print(f'Число {number} в двоичной системе будет: {new_num}')

