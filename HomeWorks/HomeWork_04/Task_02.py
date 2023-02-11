# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий
# сумму многочленов.

with open('file1 for the second task.txt', 'r', encoding='UTF-8') as polynomial:
    polynomial1 = polynomial.readline()

with open('file2 for the second task.txt', 'r', encoding='UTF-8') as polynomial:
    polynomial2 = polynomial.readline()

def convert_to_dict(polynomial: str) -> dict:
    polynomial = polynomial.replace(' + ', ' ').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
        .replace('Первый многочлен: ', '').replace('Второй многочлен: ', '').replace('*x ', '*x**1 ').split()[:-2]

    polynomial_dict = {}
    for item in polynomial:
        i = item.split('*x**')

        if len(i) > 1:
            polynomial_dict[int(i[1])] = int(i[0])
        else:
            polynomial_dict[0] = int(i[0])

    return polynomial_dict

polynomial1_dict = convert_to_dict(polynomial1)
polynomial2_dict = convert_to_dict(polynomial2)
print(polynomial1)
print(polynomial1_dict)
print(polynomial2)
print(polynomial2_dict)

def sum_dict(first_dict: dict, second_dict: dict):
    final_dict = {}
    final_dict.update(first_dict)
    final_dict.update(second_dict)

    for key in final_dict:
        final_dict[key] = first_dict.get(key, 0) + second_dict.get(key, 0)

    return final_dict
result_polynomial_dict = sum_dict(polynomial1_dict, polynomial2_dict)
print()
print(f'Результат сложения наших polynomial1_dict = {result_polynomial_dict}')

def convert_to_polynomial(result_polynomial_dict: dict) -> str:
    new_polynomial = []
    for key, value in result_polynomial_dict.items():
        if value != 0:
            new_polynomial.append(f'{value}*x**{key}')
    new_polynomial = ' + '.join(new_polynomial) + ' = 0'
    new_polynomial = new_polynomial.replace('+ -', '- ')\
        .replace(' 1*x', '  x').replace('*x**0', '').replace('x**1', 'x')
    return new_polynomial

result_polynomial = convert_to_polynomial(result_polynomial_dict)
print(f'Результат сложения наших polynomial1_dict = {result_polynomial}')

with open('result_polynomial.txt', 'w', encoding='UTF-8') as result:
    result.write('Сумма наших многочленов = ')
    result.write(result_polynomial)




