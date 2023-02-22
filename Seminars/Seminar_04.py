# Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней
# квадратного уравнения
# b2 - 4ac

import math

data = "3 * x ** 2 - 14 * x - 5 = 0"

data_list = data.split()
var_list = []

for i in range(len(data_list)):
    if data_list[i].isdigit():
        if i > 0 and data_list[i-1] == '-':
            var_list.append(-1 * int(data_list[i]))
        else:
            var_list.append(int(data_list[i]))

print(var_list)