# Задача №1. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def create_polynomialdict():
    degree = int(input('Введите максимальную степень: '))
    polynomial_dict = {}
    for i in range(degree, -1, -1):
        polynomial_dict[i] = random.randint(0, 100)
    return polynomial_dict
def convert_to_polynomial(polynomial_dict: dict) -> str:
    new_polynomial = []
    for key, value in polynomial_dict.items():
        if value != 0:
            new_polynomial.append(f'{value}*x**{key}')
    new_polynomial = ' + '.join(new_polynomial) + ' = 0'
    new_polynomial = new_polynomial.replace('+ -', '- ')\
        .replace(' 1*x', '  x').replace('*x**0', '').replace('x**1', 'x')
    return new_polynomial

polynomial = create_polynomialdict()
full_polynomial = convert_to_polynomial(polynomial)
print(full_polynomial)

with open('file2 for the second task.txt', 'w', encoding='UTF-8') as polynomial:
    polynomial.write('Второй многочлен: ')
    polynomial.write(full_polynomial)




















