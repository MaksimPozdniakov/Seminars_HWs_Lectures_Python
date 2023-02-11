# # Работаем с многочленами
import random
def create_equation():

    degree = int(input('Введите максимальную степень: '))
    equation = {}
    for n in range(degree, -1, -1):
        equation[n] = random.randint(-100, 100)
    return equation




